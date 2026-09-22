"""Continuous (passive) card effects.

A Passive is contributed by a card while it is in play: a Pokemon ability
(Ability(passive=...)), an attached Pokemon Tool, or an attached Special
Energy (both via their CardDefinition's passive=). The engine collects the
active (passive, carrier) pairs each time it computes damage, attack costs,
or max HP, so effects switch on/off purely by board position.
"""

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

from spirit.game.attributes import (AbilityTypes, AttrID, PokemonTypes,
                                    TrainerType)
from spirit.game.data_utils import ABILITIES_BY_ID, def_for, subtypes_for
from spirit.game.models.board import (
    EnergyEntity,
    BENCH_SLOT_COUNT,
    BoardEntity,
    BoardState,
    CardEntity,
    PokemonEntity,
    board_of,
)

WEAKNESS_MULTIPLIER = 2
# Fallback only: a card's own RESISTANCE_AMOUNT wins when it has one.
# Every printing in the pool today is -30, but SM-era cards print -20.
RESISTANCE_REDUCTION = 30

# Areas whose top-level cards keep a temporary passive alive.
_IN_PLAY_AREAS = ("activePokemonArea", "bench", "activeStadium")


@dataclass
class TurnDamageModifier:
    """A turn-scoped attacker-side damage boost (Power Tablet: "+30 damage
    during this turn to your Fusion Strike Pokemon's attacks")."""
    amount: int
    player_id: str
    requires_subtype: Optional[str] = None
    opposing_active_only: bool = True
    # None = this turn only; otherwise the last turn number it still applies.
    expires_after_turn: Optional[int] = None
    # "For the rest of this game" (Altered Creation-GX): never pruned.
    permanent: bool = False
    # Only while THIS entity attacks (Scyther's next-turn self boost).
    source_entity_id: Optional[str] = None
    # Only while resolving this attack title (Metagross' Fullmetal Impact rider).
    attack_title: Optional[str] = None
    # Arbitrary attacker gate (Ludicolo/Rapidash predicates).
    source_predicate: Optional[Callable[[BoardEntity], bool]] = None


@dataclass
class TempPassive:
    """An effect-granted passive with a lifetime. expires_after_turn None =
    until the carrier leaves the Active spot / play (clear_pokemon_effects)."""
    passive: "Passive"
    carrier_entity_id: str
    expires_after_turn: Optional[int] = None
    # Granted by an attack (Pokemon Ranger removes these and nothing else).
    from_attack: bool = False


class DamageCalc:
    """One damage computation, mutated in stages by the passive hooks."""

    def __init__(
        self,
        board: BoardState,
        attacker: Optional[BoardEntity],
        target: PokemonEntity,
        base: int,
        is_attack: bool = True,
        apply_modifiers: bool = True,
        ignore_target_effects: bool = False,
        attack_title: Optional[str] = None,
    ):
        self.board = board
        self.attacker = attacker
        self.target = target
        self.base = base
        self.amount = base
        # True for attack damage; False for ability/effect damage.
        self.is_attack = is_attack
        # Weakness/Resistance stage runs only versus the defending Active.
        self.apply_modifiers = apply_modifiers
        # Title of the attack being resolved (matches TurnDamageModifier riders).
        self.attack_title = attack_title
        self.weakness_applies = True
        self.weakness_multiplier = WEAKNESS_MULTIPLIER
        # Rewritable by modify_weakness hooks (Spiritomb/UnownVSTAR overrides).
        self.weak_types: List[Any] = list(
            target.get_attribute(AttrID.WEAKNESS_TYPES) or []
        )
        self.resistance_applies = True
        self.weakness_hit = False
        self.resistance_hit = False
        self.prevented = False
        # Max Miracle-style: skip passives riding the DEFENDING Pokemon in the
        # taken/prevention stages (attacker-side and third-party still run).
        self.ignore_target_effects = ignore_target_effects
        # Scratch set for non-stacking effects (e.g. Lesson in Zeal) to mark
        # themselves applied and skip on a later pass within the same calc.
        self.applied_once: Set[str] = set()

    @property
    def to_active(self) -> bool:
        """Whether the target sits in its owner's Active spot."""
        parent = self.target.parent
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "activePokemonArea"

    @property
    def is_opposing(self) -> bool:
        """Whether attacker and target belong to different players."""
        return (
            self.attacker is not None
            and self.attacker.owning_player_id != self.target.owning_player_id
        )


class Passive:
    """Override only the hooks a card's continuous effect needs.

    `carrier` is the entity contributing the passive: the Pokemon whose
    ability it is, or the attached tool/energy card (carrier_pokemon gives
    the Pokemon an attachment rides on).
    """

    # Same-key passives count once in effective_max_hp (Abomasnow stacks).
    stacking_key: Optional[str] = None

    # For a passive on an Energy card that can RAISE how much that card
    # provides at once (Ignition to 3, Neo Upper to 2): the ceiling, so the
    # attachment pip can be cropped to show that many emblems. Purely
    # cosmetic -- modify_energy_provided is what actually pays costs. Leave
    # None on a passive that only changes the TYPES provided and not the
    # count (Prism Energy stays 1 at a time, so it stays one emblem).
    max_energy_provided: Optional[int] = None

    # Optional awaitable damage stage: async (ctx, calc, target, carrier) ->
    # Optional[int], consulted in ctx.deal_damage AFTER compute_damage and
    # BEFORE the HP write (None = unchanged, else the new dealt amount).
    # Flip-to-prevent (Infiltrator) and KO-survive (Guts) live here; may queue
    # coin flips via ctx so they choreograph inside the attack bracket.
    damage_interceptor: Optional[Any] = None

    # Optional awaitable post-attack stage: async (ctx, carrier) -> None, run
    # by resolve_attack AFTER knockouts/deferred actions resolve (end-of-turn
    # riders like Blunder Policy); queued messages flush as their own brackets.
    attack_followup: Optional[Any] = None

    def modify_damage_dealt(self, calc: DamageCalc, carrier: BoardEntity):
        """Attacker-side "does more/less damage" step (runs before W/R)."""

    def modify_weakness(self, calc: DamageCalc, carrier: BoardEntity):
        """May clear calc.weakness_applies (e.g. "... have no Weakness"), or
        rewrite calc.weak_types / calc.weakness_multiplier."""

    def modify_resistance(self, calc: DamageCalc, carrier: BoardEntity):
        """May clear calc.resistance_applies ("... has no Resistance")."""

    def modify_damage_taken(self, calc: DamageCalc, carrier: BoardEntity):
        """Defender-side "takes less damage" step (runs after W/R)."""

    def prevents_damage(self, calc: DamageCalc, carrier: BoardEntity) -> bool:
        """True to prevent the hit entirely (calc.amount becomes 0)."""
        return False

    def applies_bench_modifiers(self, calc: DamageCalc, carrier: BoardEntity) -> bool:
        """True to run Weakness/Resistance on a hit that skipped them only
        because its target is Benched -- the rules parenthetical "(Don't
        apply Weakness and Resistance for Benched Pokemon.)" -- Wide Lens.
        An attack whose own text says its damage "isn't affected by
        Weakness or Resistance" (ignore_weakness / ignore_resistance) stays
        unaffected: those flags live on the calc, not on this switch."""
        return False

    def modify_attack_cost(
        self,
        cost: Dict[str, int],
        pokemon: PokemonEntity,
        carrier: BoardEntity,
        board: BoardState,
    ) -> Dict[str, int]:
        """Returns the (possibly reduced) cost dict, client-name keyed."""
        return cost

    def max_hp_bonus(self, pokemon: PokemonEntity, carrier: BoardEntity) -> int:
        """Extra max HP granted to `pokemon` (e.g. Heat Fire Energy's +20)."""
        return 0

    def modify_retreat_cost(
        self, cost: int, pokemon: PokemonEntity, carrier: BoardEntity,
        board: BoardState,
    ) -> int:
        """Returns the (possibly reduced) retreat cost (Air Balloon's -2);
        `board` lets stadium-gated hooks read global state (Thwackey)."""
        return cost

    def blocks_attack_effects(self, target: PokemonEntity, carrier: BoardEntity,
                              source: Optional[PokemonEntity] = None) -> bool:
        """True to shield `target` from opponents' attack EFFECTS (not damage).

        `source` is the attacking Pokemon when the caller knows it, for the
        shields that only answer to certain attackers (Alolan Persian-GX);
        shields that do not care ignore it.
        """
        return False

    def blocks_abilities(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to turn off `pokemon`'s Abilities (Path to the Peak style)."""
        return False

    def blocks_ability(self, pokemon: PokemonEntity, ability, carrier: BoardEntity) -> bool:
        """True to take ONE named Ability away from `pokemon` (Psyduck's
        Damp: "lose any Ability that requires the Pokemon using it to Knock
        Out itself"), leaving its other Abilities alone."""
        return False

    def blocks_trainer_targeting(self, target: BoardEntity, carrier: BoardEntity) -> bool:
        """True to shield `target` from being touched by Item and Supporter
        cards at all (Thunder Mountain shields itself from Field Blower).

        Distinct from blocks_trainer_effects, which is Dew Guard's
        player-scoped shield against a specific Trainer's effects.
        """
        return False

    def blocks_out_of_play_abilities(
        self, card: BoardEntity, carrier: BoardEntity
    ) -> bool:
        """True to turn off the Abilities of `card` while it sits in a hand or
        a discard pile (Garbotoxin).

        Separate from blocks_abilities because almost every lock is worded
        "Pokemon in play" and must NOT reach these zones; only a lock that
        names them implements this.
        """
        return False

    def blocks_attacking(self, pokemon: PokemonEntity, carrier: BoardEntity,
                         board: BoardState) -> bool:
        """True to stop `pokemon` using any attack at all (Vileplume's
        Disgusting Pollen, Slaking ex's Born to Slack). `board` comes along
        because these read the whole table. Per-attack refusals belong on the
        Attack's own condition, and turn-scoped ones on TurnState.lock_attack."""
        return False

    def blocks_retreat(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to forbid `pokemon` from retreating (Octolock, Flygon)."""
        return False

    def attacks_first_turn(self, pokemon: PokemonEntity,
                           carrier: BoardEntity) -> bool:
        """True to lift the "no attacking on turn 1 going first" rule for
        `pokemon` (Meloetta ex's Debut Performance). The per-attack form of
        the same permission is the Attack's own usable_first_turn."""
        return False

    def attacks_despite_conditions(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to let `pokemon` attack even while Asleep/Paralyzed (Windup Arm)."""
        return False

    def mega_evolution_keeps_turn(self, pokemon: PokemonEntity,
                                  carrier: BoardEntity) -> bool:
        """True to waive the Mega Evolution rule's "your turn ends" for
        `pokemon` becoming a Mega Evolution Pokemon (a Spirit Link Tool
        attached to it). Nothing in the pool says so yet."""
        return False

    def sleep_checkup_coins(self, pokemon: PokemonEntity, carrier: BoardEntity) -> int:
        """How many coins `pokemon` flips to wake up at Checkup under this
        passive (Slumbering Forest: 2). 0 = no opinion; the largest answer
        wins, and every coin has to be heads."""
        return 0

    def supporter_play_limit(self, player_id: str, carrier: BoardEntity) -> int:
        """How many Supporter cards `player_id` may play in a turn under this
        passive (Magnezone's Dual Brains: 2). 0 = no opinion; the largest
        answer wins, the rule's own 1 is the floor -- two Dual Brains do not
        make 3."""
        return 0

    def retreats_despite_conditions(self, pokemon: PokemonEntity,
                                    carrier: BoardEntity) -> bool:
        """True to let `pokemon` retreat even while Asleep/Paralyzed
        (Escape Board). The retreat cost itself is unaffected."""
        return False

    def discard_destination(self, card: BoardEntity,
                            carrier: BoardEntity) -> Optional[str]:
        """Player-area name replacing "discard" for `card` when it is
        discarded FROM PLAY (U-Turn Board's "put it into your hand instead
        of the discard pile"). None for the ordinary discard.

        Only asked of cards leaving play: the same card discarded out of a
        hand or a deck goes to the discard pile like any other.
        """
        return None

    def blocks_special_conditions(
        self, target: PokemonEntity, condition: Any, carrier: BoardEntity
    ) -> bool:
        """True to shield `target` from having `condition` applied to it."""
        return False

    def prevents_healing(self, target: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to prevent healing damage from `target` (Mimikyu SWSH3)."""
        return False

    def heal_multiplier(self, target: PokemonEntity, carrier: BoardEntity) -> int:
        """Factor applied to heal amounts (Legendary Ocean Trench's 2)."""
        return 1

    def knockout_destination(self, pokemon: PokemonEntity, carrier: BoardEntity) -> Optional[str]:
        """Area name replacing "discard" for a knocked-out Pokemon (e.g. "lostZone")."""
        return None

    def modify_prizes_for_knockout(
        self, pokemon: PokemonEntity, ctx: Any, count: int, carrier: BoardEntity
    ) -> int:
        """Prize count the opponent takes for knocking out `pokemon` (Komala);
        evaluated BEFORE the stack moves, so board/conditions still count."""
        return count

    async def extra_prizes_for_knockout(
        self, pokemon: PokemonEntity, ctx: Any, count: int, carrier: BoardEntity
    ) -> int:
        """Extra prizes to add after sync modifiers (Togekiss Wonder Kiss coin
        flip). Return the bonus amount, not a new total. stacking_key is
        honored by the knockout resolver so copies don't stack."""
        return 0

    def prize_destination(
        self, pokemon: PokemonEntity, ctx: Any, carrier: BoardEntity
    ) -> Optional[str]:
        """Area name replacing "hand" for the prizes taken for this knockout
        ("discard" = Billowing Smoke, "lostZone" = Barbaracle)."""
        return None

    def modify_energy_provided(
        self, options: List[List[int]], energy: BoardEntity,
        holder: Optional[PokemonEntity], board: BoardState,
    ) -> List[List[int]]:
        """Rewrites an energy's provided-type options (Charizard PGO doubling)."""
        return options

    def modify_pokemon_types(
        self, types: List[Any], pokemon: BoardEntity, carrier: BoardEntity
    ) -> List[Any]:
        """Rewrites `pokemon`'s live type list (Kecleon's Chromashift)."""
        return types

    def blocks_energy_removal(
        self, energy: BoardEntity, mover_player_id: str, carrier: BoardEntity
    ) -> bool:
        """True to keep an attached Energy from being moved to hand/deck/
        discard by `mover_player_id`'s Item/Supporter effect (Brazen Tail)."""
        return False

    def suppresses_special_energy(self, energy: BoardEntity, carrier: BoardEntity) -> bool:
        """True to neutralize a Special Energy (Temple of Sinnoh): it loses
        its passive and provides only Colorless."""
        return False

    def suppresses_tool(self, tool: BoardEntity, carrier: BoardEntity) -> bool:
        """True to neutralize an attached Pokemon Tool's passive hooks
        (Tool Jammer); evaluated on the unfiltered set like ability locks."""
        return False

    def granted_attacks(
        self, board: BoardState, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> List[Any]:
        """Extra Attack definitions `pokemon` may use (Ditto's Sudden
        Transformation, Memory Capsule); costs/locks still apply normally."""
        return []

    def granted_attacks_with_owner(
        self, board: BoardState, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> List[Any]:
        """The same grants as (owner card, attack) pairs -- the owner is the
        card the attack is printed on, whose type colours the row when the
        grants are listed in the scroll panel. Default: the Pokemon itself
        (Memory Energy gives back its own line's attacks)."""
        return [(pokemon, a) for a in (self.granted_attacks(board, pokemon, carrier) or [])]

    def blocks_putting_into_play(
        self, card: BoardEntity, player_id: str, carrier: BoardEntity
    ) -> bool:
        """"You can't put <cards> into play" (Eternal Zone): asked of every
        way a Pokemon enters play from outside it -- a Basic or fossil
        played from hand, a Bench put by a search or an Ability, an
        identity swap (Thorton) -- never of evolving or promoting, which
        happen to a Pokemon already in play."""
        return False

    def blocks_trainer_play(
        self, card: BoardEntity, player_id: str, carrier: BoardEntity
    ) -> bool:
        """True to forbid `player_id` playing `card` from hand (Vileplume)."""
        return False

    def may_evolve_early(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to exempt `pokemon` from the just-played/first-turn evolution
        gates (Caterpie's Adaptive Evolution)."""
        return False

    def may_evolve_same_turn(
        self, pokemon: PokemonEntity, carrier: BoardEntity, evolution_card: BoardEntity
    ) -> bool:
        """True to skip the just-played evolution gate (not the first-turn
        gate) when playing `evolution_card` onto `pokemon` (Forest of Vitality)."""
        return False

    def may_be_evolved_into(
        self, pokemon: PokemonEntity, carrier: BoardEntity, evolution_card: BoardEntity
    ) -> bool:
        """True to let `evolution_card` evolve onto `pokemon` even when
        EVOLUTION_LOGIC_NAME does not match (Eevee ex Rainbow DNA)."""
        return False

    def blocks_evolution(
        self, player_id: str, target: PokemonEntity, carrier: BoardEntity
    ) -> bool:
        """True to forbid `player_id` evolving `target` at all (Dracovish)."""
        return False

    def modify_burn_counters(
        self, counters: int, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> int:
        """Damage counters the Burn checkup tick places (default 2)."""
        return counters

    def modify_poison_counters(
        self, counters: int, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> int:
        """Damage counters the Poison checkup tick places (default 1, or the
        Pokémon's recorded poison_counters). Pecharunt's Toxic Subjugation."""
        return counters

    def blocks_burn_recovery(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to skip the Burn recovery flip entirely (stays Burned)."""
        return False

    def forces_coin_tails(self, flipper_id: str, carrier: BoardEntity) -> bool:
        """True to make every coin `flipper_id` flips during their own turn
        land tails (Malamar's Contrary). Asked of card-effect flips and the
        in-turn rule flips (Confusion, Smokescreen, an attach tax); never of
        the Pokemon Checkup or the opening flip."""
        return False

    def tool_capacity(self, pokemon: PokemonEntity, carrier: BoardEntity) -> int:
        """Pokemon Tools `pokemon` may hold (GarbodorVMAX 2); highest wins."""
        return 1

    def bench_capacity(self, player_id: str, carrier: BoardEntity) -> Optional[int]:
        """Bench size override for `player_id` (Collapsed Stadium 4); None =
        no opinion, the smallest override wins."""
        return None

    def player_visualizations(
        self, player_id: str, carrier: BoardEntity
    ) -> List[Dict[str, Any]]:
        """Persistent status rows shown on `player_id`'s side of the playmat
        (attr 200370 on their PlayerEntity), as opposed to the turn-scoped PiPs
        add_turn_stat_visualization puts on a Pokemon.

        Return the viz dicts this passive contributes for that player. They are
        recomputed from scratch whenever the board settles, so a passive that
        stops applying simply stops returning them -- there is no teardown.

        No card uses this yet, and the one attempt crashed the client:
        `displayType` must name a real VisualizationTypes member, because the
        client parses it into the enum and dereferences the result unguarded.
        A row carrying anything else -- a card-specific name taken from a
        LocalizationDB key, say -- throws NullReferenceException inside the
        sequence handling, not at the rendering site."""
        return []

    # True when the extra attack this passive hands out is limited to attacks
    # the Pokemon HAS (Festival Lead), which a Tool or Energy lending one of
    # its own is not. Jumpluff's "may attack twice" says no such thing, so it
    # leaves this False and any attack on the panel counts.
    extra_attack_printed_only: bool = False

    def attack_keeps_turn(self, attacker: PokemonEntity, ability: Any,
                          ctx: Any, carrier: BoardEntity) -> bool:
        """True to keep the turn going after `attacker`'s attack resolved
        (Fluffy Barrage); runs after knockouts resolve, so KO evidence rides
        ctx.knockouts_resolved, not ctx.knockouts."""
        return False

    def blocks_ability_effects(self, target: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to shield `target` from opponents' Ability effects (Corviknight VMAX)."""
        return False

    def blocks_damage_counters(self, target: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to prevent damage counters (not attack damage) on `target`
        (Battle Cage's benched-Pokémon shield)."""
        return False

    def blocks_moving_damage_counters(self, carrier: BoardEntity) -> bool:
        """True to forbid moving damage counters between Pokémon (Patrat)."""
        return False

    def blocks_discard(self, card: BoardEntity, carrier: BoardEntity) -> bool:
        """True to keep `card` from being discarded by an opponent's effect."""
        return False

    def blocks_discard_recovery(self, player_id: str, carrier: BoardEntity) -> bool:
        """True to keep `player_id` from putting cards from THEIR discard
        pile into their hand with an Ability or Trainer card (Toedscruel's
        Slime Mold Colony). Attacks are not named, so they still can."""
        return False

    def blocks_tool_attach(self, player_id: str, carrier: BoardEntity) -> bool:
        """True to keep `player_id` from attaching Pokemon Tool cards from
        their hand (Goodra's Slip Trip, both players)."""
        return False

    def turn_draw_count(self, player_id: str, count: int,
                        carrier: BoardEntity) -> int:
        """Rewrites how many cards `player_id` draws at the start of their
        turn (Hall of Fame Belt: 2 while its holder is Active)."""
        return count

    def blocks_player_attack_effects(self, player_id: str,
                                     carrier: BoardEntity) -> bool:
        """True to shield `player_id` and their HAND from the effects of an
        opposing Pokemon's attack (Marowak's Bodyguard): play locks, hand
        discards / shuffles / bottom-decking, forced draws. Effects done to
        a Pokemon are a different question (blocks_attack_effects)."""
        return False

    def blocks_trainer_effects(
        self, affected_player_id: str, trainer_card: BoardEntity,
        trainer_type: Any, carrier: BoardEntity,
        affected_entity: Optional[BoardEntity] = None,
        board: Optional["BoardState"] = None,
    ) -> bool:
        """True to shield `affected_player_id`'s side from an opposing trainer
        card's effects (Dew Guard); trainer_type is the TrainerType value.
        affected_entity is the primitive's direct object (None for
        player-level effects like draws/hand shuffles)."""
        return False

    def replace_supporter_effect(
        self, card: BoardEntity, player_id: str, carrier: BoardEntity
    ) -> Optional[Any]:
        """Replacement effect coroutine for `player_id`'s Supporter `card`
        (Shifty Substitution); None = no replacement."""
        return None

    def taxes_energy_attach(
        self, attaching_player_id: str, energy: BoardEntity,
        target: PokemonEntity, carrier: BoardEntity,
    ) -> bool:
        """True to coin-flip `attaching_player_id`'s manual energy attach
        (Slimy Room): tails discards the energy instead of attaching."""
        return False

    def retreat_cost_destination(
        self, pokemon: PokemonEntity, energy: BoardEntity, carrier: BoardEntity
    ) -> Optional[str]:
        """Player-area name replacing "discard" for `energy` paid for
        `pokemon`'s retreat (Skaters' Park sends basic Energy to "hand")."""
        return None

    def counters_on_active_to_bench(
        self, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> int:
        """Damage counters put on an Active that moved to its owner's Bench
        during that owner's turn (Spikemuth)."""
        return 0

    def heal_on_evolve(
        self, evolved: PokemonEntity, pre_evolution: BoardEntity,
        player_id: str, carrier: BoardEntity,
    ) -> int:
        """Damage healed from a Pokemon `player_id` just evolved from hand
        (Wyndon Stadium)."""
        return 0

    def offers_attack_coin_reroll(
        self, player_id: str, carrier: BoardEntity, attacker: Optional[BoardEntity] = None
    ) -> bool:
        """True to let `player_id` re-flip an attack's coins once during
        their turn (Glimwood Tangle / Backtrack Badge). `attacker` is the
        Pokemon whose attack flipped the coins, when known."""
        return False

    def stadium_immunity(self, board: BoardState, carrier: BoardEntity) -> bool:
        """New Moon: True while this passive asks for its owner's Pokemon in
        play to be shielded from every Stadium effect ("If you have Solrock
        in play, prevent all effects of any Stadium done to your Pokemon in
        play"). The shield is stateful -- see _refresh_stadium_shields -- so
        the answer here is only the printed condition, not the lock check."""
        return False


def carrier_pokemon(carrier: BoardEntity) -> Optional[PokemonEntity]:
    """The in-play Pokemon a passive rides: the carrier itself, or the
    top-level Pokemon its attachment stack hangs under."""
    entity = carrier
    while entity is not None:
        parent = entity.parent
        if isinstance(entity, PokemonEntity) and not isinstance(parent, CardEntity):
            return entity
        entity = parent if isinstance(parent, CardEntity) else None
    return None


# --- New Moon: a side's Pokemon in play ignore every Stadium effect --------
#
# Lunatone's New Moon is the only printed shield against Stadium effects, and
# the official Q&A makes it ORDER-DEPENDENT: Silent Lab played onto a working
# New Moon is itself a Stadium effect and gets prevented, while a Lunatone
# put into play under Silent Lab has no Ability to shield anyone with. So the
# shield is a piece of state (board.stadium_shields: Lunatone entity id ->
# owner) that flips on when the printed condition is met AND the Ability is
# not locked at that moment (Stadium locks still reach it), and flips off
# when the condition fails or a NON-Stadium lock (Garbotoxin) reaches it --
# Stadium locks can't, because the shield is up. Stealthy Hood needs nothing
# extra: _locks_abilities_of already ignores an opponent's Ability lock on
# its holder, so Garbotoxin never switches a hooded Lunatone off.

# Stadium hooks that read as an effect on the PLAYER (or the coin) even
# though a Pokemon rides along in the arguments; the official Q&A lets a
# New Moon player re-flip under Luminous Maze Forest.
_STADIUM_PLAYER_HOOKS = frozenset({
    "offers_attack_coin_reroll", "player_visualizations", "bench_capacity",
    "supporter_play_limit", "turn_draw_count", "blocks_trainer_play",
    "blocks_discard_recovery", "blocks_tool_attach",
    "blocks_player_attack_effects", "replace_supporter_effect",
    "blocks_moving_damage_counters", "blocks_out_of_play_abilities",
})
# Hooks whose first argument is an attached card: the effect lands on the
# Pokemon it is attached to (Temple of Sinnoh under New Moon leaves
# Luminous Energy providing every type, per the Q&A).
_STADIUM_ATTACHMENT_HOOKS = frozenset({
    "discard_destination", "suppresses_special_energy", "suppresses_tool",
    "blocks_energy_removal",
})


def _stadium_hook_target(name: str, args, kwargs) -> Optional[PokemonEntity]:
    """The in-play Pokemon a Stadium hook call is an effect on, or None when
    the call is not about any particular Pokemon."""
    if name in _STADIUM_PLAYER_HOOKS:
        return None
    values = list(args) + list(kwargs.values())
    if values and isinstance(values[0], DamageCalc):
        calc = values[0]
        entity = calc.attacker if name == "modify_damage_dealt" else calc.target
        return entity if isinstance(entity, PokemonEntity) else None
    for value in values:
        if isinstance(value, PokemonEntity):
            return value
    if name in _STADIUM_ATTACHMENT_HOOKS and values:
        return carrier_pokemon(values[0]) if isinstance(values[0], BoardEntity) else None
    return None


def stadium_effects_prevented(board: BoardState, pokemon: BoardEntity) -> bool:
    """Whether `pokemon` (in play) is shielded from Stadium effects by a
    working New Moon on its side. Card scripts use it for the Stadium
    effects that are not passives (Gapejaw Bog's counters, Crystal Cave's
    heal); EffectContext consults it for every Stadium-sourced primitive."""
    if not isinstance(pokemon, PokemonEntity):
        return False
    _collect_passives(board)  # refreshes the shields for the current board
    if pokemon.owning_player_id not in (getattr(board, "stadium_shield_players", None) or ()):
        return False
    return pokemon._containing_area_name() in ("activePokemonArea", "bench")


def _shielded(board: BoardState, target: PokemonEntity) -> bool:
    players = getattr(board, "stadium_shield_players", None)
    if not players or target.owning_player_id not in players:
        return False
    return target._containing_area_name() in ("activePokemonArea", "bench")


class _StadiumGuard(Passive):
    """Wraps a Stadium's passive: every hook whose target Pokemon is under a
    New Moon shield answers with the Passive base default instead."""

    def __init__(self, inner: Passive, board: BoardState):
        self.inner = inner
        self.board = board

    def __getattr__(self, name):
        return getattr(self.inner, name)


def _make_stadium_guard_hook(name, base_fn):
    def hook(self, *args, **kwargs):
        target = _stadium_hook_target(name, args, kwargs)
        if target is not None and _shielded(self.board, target):
            return base_fn(self.inner, *args, **kwargs)
        return getattr(self.inner, name)(*args, **kwargs)
    hook.__name__ = name
    return hook


for _name, _fn in list(vars(Passive).items()):
    if callable(_fn) and not _name.startswith("_") and _name != "stadium_immunity":
        setattr(_StadiumGuard, _name, _make_stadium_guard_hook(_name, _fn))


def _stateful_archetypes() -> Tuple[Set[str], Set[str]]:
    """(stadium-immunity archetypes, Ability-lock archetypes): the cards
    whose Abilities carry state that must be settled against the board
    before every change; cached against the size of the card registry."""
    global _IMMUNITY_CACHE
    from spirit.game.data_utils import CARD_DEFS_BY_GUID
    size = len(CARD_DEFS_BY_GUID)
    if _IMMUNITY_CACHE is None or _IMMUNITY_CACHE[0] != size:
        immune, locks = set(), set()
        for guid, definition in CARD_DEFS_BY_GUID.items():
            for ability in getattr(definition, "abilities", None) or []:
                passive = getattr(ability, "passive", None)
                if passive is None:
                    continue
                if type(passive).stadium_immunity is not Passive.stadium_immunity:
                    immune.add(guid)
                if type(passive).blocks_abilities is not Passive.blocks_abilities:
                    locks.add(guid)
        _IMMUNITY_CACHE = (size, immune, locks)
    return _IMMUNITY_CACHE[1], _IMMUNITY_CACHE[2]


def _stadium_immunity_archetypes() -> Set[str]:
    return _stateful_archetypes()[0]


_IMMUNITY_CACHE: Optional[Tuple[int, Set[str], Set[str]]] = None


def _settle_stadium_shields_before_change(board: BoardState) -> None:
    """BoardState pre-change hook: with a New Moon Pokemon in play, decide
    the shields against the board as it stands before the next card moves,
    so "Silent Lab played onto a working New Moon" and "Lunatone put into
    play under Silent Lab" come out differently even when nothing queried
    the passives in between."""
    if not getattr(board, "player_ids", None):
        return
    immune, locks = _stateful_archetypes()
    stateful = immune | locks
    if not stateful:
        return
    for player_id in board.player_ids:
        for pokemon in board.pokemon_in_play(player_id):
            if (pokemon.archetype_id or "").lower() in stateful:
                _collect_passives(board)
                return
    if getattr(board, "stadium_shields", None):
        board.stadium_shields.clear()
        board.stadium_shield_players = frozenset()
    if getattr(board, "ability_lock_seq", None):
        board.ability_lock_seq.clear()


BoardState.pre_change_hooks.append(_settle_stadium_shields_before_change)


def _refresh_stadium_shields(
    board: BoardState,
    triples: List[Tuple[Passive, BoardEntity, bool]],
    stadium_triples: List[Tuple[Passive, BoardEntity, bool]],
) -> None:
    """State-based update of board.stadium_shields (see the note above)."""
    shields = getattr(board, "stadium_shields", None)
    if shields is None:
        shields = {}
        board.stadium_shields = shields
    seen = set()
    non_stadium = None
    for passive, carrier, is_ability in triples:
        if type(passive).stadium_immunity is Passive.stadium_immunity:
            continue
        key = carrier.entity_id
        seen.add(key)
        owner = carrier.owning_player_id
        condition = passive.stadium_immunity(board, carrier)
        if non_stadium is None:
            non_stadium = [t for t in triples
                           if not any(t is st for st in stadium_triples)]
        if key in shields:
            # Up: only the condition failing or a non-Stadium lock ends it.
            if not condition or (is_ability and _locks_abilities_of(non_stadium, carrier)):
                del shields[key]
            continue
        if not condition:
            continue
        # Down: Stadium locks still reach this Pokemon -- unless a sibling
        # shield on the same side is already up and covering it.
        pool = non_stadium if owner in shields.values() else triples
        if is_ability and _locks_abilities_of(pool, carrier):
            continue
        shields[key] = owner
    for key in [k for k in shields if k not in seen]:
        del shields[key]
    board.stadium_shield_players = frozenset(shields.values())


def _scanning_passives(board: BoardState) -> bool:
    """True while a passive scan is settling lock state or filtering the
    live set. A hook that asks the board a passive-dependent question from
    inside that scan (Bide Barricade reading a Pokemon's live types) must
    not start another scan: effective_pokemon_types answers with the
    printed types instead."""
    return bool(getattr(board, "_passive_scan_depth", 0))


def _collect_passives(board: BoardState) -> List[Tuple[Passive, BoardEntity, bool]]:
    """All (passive, carrier, is_ability) triples currently switched on by
    board position, before ability locks are applied. is_ability is True only
    for passives contributed by a Pokemon's own PIE_ABILITIES entry."""
    triples: List[Tuple[Passive, BoardEntity, bool]] = []
    for player_id in board.player_ids:
        for pokemon in board.pokemon_in_play(player_id):
            # Card-level PokemonCardDef(passive=): rules text that is not an
            # Ability, so ability locks never switch it off.
            card_passive = getattr(def_for(pokemon.archetype_id), "passive", None)
            if card_passive is not None:
                triples.append((card_passive, pokemon, False))
            for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
                if not isinstance(entry, dict):
                    continue
                ability = ABILITIES_BY_ID.get(entry.get("abilityID"))
                if ability is not None and ability.passive is not None:
                    # A Tool-granted ability's passive rides the tool, not the
                    # Pokemon, so Path to the Peak can't switch it off; an
                    # Ancient Trait is not an Ability at all, and Garbotoxin,
                    # Silent Lab and Path to the Peak each name Abilities.
                    lockable = (not ability.is_granted
                                and ability.ability_type != AbilityTypes.ANCIENT_TRAIT)
                    triples.append((ability.passive, pokemon, lockable))
            for attachment in _descendants(pokemon):
                # Tucked pre-evolutions contribute nothing; a Pokemon card
                # attached "as a Pokemon Tool" (Klefki's Wonder Lock) is a
                # Tool here and its card passive rides it like a Tool's.
                if isinstance(attachment, PokemonEntity) \
                        and not getattr(attachment, "acts_as_tool", False):
                    continue
                definition = def_for(attachment.archetype_id)
                passive = getattr(definition, "passive", None)
                if passive is not None:
                    triples.append((passive, attachment, False))
    stadium_area = board.find_global_area("activeStadium")
    stadium_triples: List[Tuple[Passive, BoardEntity, bool]] = []
    for stadium in (stadium_area.children if stadium_area else []):
        definition = def_for(stadium.archetype_id)
        passive = getattr(definition, "passive", None)
        if passive is not None:
            stadium_triples.append((passive, stadium, False))
    triples.extend(stadium_triples)
    # "For the rest of this game" passives (Full Metal Wall-GX): owned by a
    # PLAYER rather than by a card, so they outlive the Pokemon that made
    # them and nothing on the board can switch them off. The owner's Active
    # area stands in as the carrier -- these passives carry their own owner
    # id and must not read the carrier.
    for passive, owner_id in getattr(board, "game_passives", None) or []:
        anchor = board.find_player_area(owner_id, "activePokemonArea")
        if anchor is not None:
            triples.append((passive, anchor, False))
    # Effect-granted temporary passives; dead carriers are silently skipped.
    for temp in getattr(board, "temporary_passives", None) or []:
        carrier = board.get_entity(temp.carrier_entity_id)
        if carrier is None or not _carrier_in_play(carrier):
            continue
        triples.append((temp.passive, carrier, False))
    # Mutual Ability locks (Klefki vs Flutter Mane): the one that started
    # working first wins, so which locks are live is state. The refresh
    # asks every lock passive whom it would lock, and a lock keyed on a
    # LIVE type (Bide Barricade's "except for Psychic Pokemon" reads
    # effective_pokemon_types) comes straight back here for the passives
    # -- so a nested collect skips the state refreshes and answers from
    # the state the outer pass is in the middle of settling.
    if not _scanning_passives(board):
        board._passive_scan_depth = 1
        try:
            _refresh_ability_lock_seq(board, triples)
            # New Moon: decide the shields on the raw set, then hand out
            # the Stadium passives behind a guard that honours them.
            _refresh_stadium_shields(board, triples, stadium_triples)
        finally:
            board._passive_scan_depth = 0
    if stadium_triples and getattr(board, "stadium_shield_players", None):
        guarded = {id(t): (_StadiumGuard(t[0], board), t[1], t[2]) for t in stadium_triples}
        triples = [guarded.get(id(t), t) for t in triples]
    return triples


def _carrier_in_play(entity: BoardEntity) -> bool:
    """Whether an entity (or the stack it is attached under) sits in play."""
    node = entity
    while isinstance(getattr(node, "parent", None), CardEntity):
        node = node.parent
    parent = getattr(node, "parent", None)
    return parent is not None \
        and parent.get_attribute(AttrID.NAME) in _IN_PLAY_AREAS


def _non_ability_locked(
    triples: List[Tuple[Passive, BoardEntity, bool]], target: BoardEntity
) -> bool:
    """A lock that is NOT an Ability (Path to the Peak, Silent Lab) reaches
    `target`; shields against Ability effects do not apply to those."""
    return any(p.blocks_abilities(target, c)
               for p, c, from_ability in triples if not from_ability)


def _ability_effect_shielded(
    triples: List[Tuple[Passive, BoardEntity, bool]], pokemon: PokemonEntity
) -> bool:
    """`pokemon` is shielded from the OPPONENT's Ability effects: by a Tool
    (Stealthy Hood) or by an Ability of its own (Hide 'n' Sneak, Luminous
    Wing) that no non-Ability lock has switched off."""
    for p, c, from_ability in triples:
        if not p.blocks_ability_effects(pokemon, c):
            continue
        if from_ability and _non_ability_locked(triples, carrier_pokemon(c) or c):
            continue
        return True
    return False


def _refresh_ability_lock_seq(
    board: BoardState, triples: List[Tuple[Passive, BoardEntity, bool]]
) -> None:
    """State-based update of board.ability_lock_seq: Pokemon entity id ->
    the order in which its Ability lock started WORKING (it is switched on
    and, by position, has something to lock).

    Two Ability locks that would each switch the other off (Klefki's
    Mischievous Lock vs Flutter Mane's Midnight Fluttering) resolve by that
    order: the earlier one is live, the later one never comes on. Locks
    that come on in the same pass are ordered by turn order from the first
    player -- at setup the Actives are revealed together and the first
    player's Ability works first (official ruling). A lock that stops
    working (locked by a non-Ability lock, by an earlier live lock, its
    carrier leaving play or the Active Spot) loses its place and queues
    anew if it comes back.
    """
    seq = getattr(board, "ability_lock_seq", None)
    if seq is None:
        seq = {}
        board.ability_lock_seq = seq
    ts = getattr(board, "turn_state", None)
    if ts is not None and getattr(ts, "turn_number", 0) == 0:
        # Setup: the opening Actives are revealed together, so nothing
        # placed before turn 1 is "earlier" -- every pass re-ranks from
        # scratch and the first player's tie-break decides.
        seq.clear()
    in_play = [p for pid in board.player_ids for p in board.pokemon_in_play(pid)]
    candidates = [(p, c) for p, c, is_ability in triples
                  if is_ability and isinstance(c, PokemonEntity)
                  and type(p).blocks_abilities is not Passive.blocks_abilities]
    if not candidates:
        seq.clear()
        return

    def would_lock(p, c, target):
        return target is not c and p.blocks_abilities(target, c)

    # Turn order from the first player for the ties.
    first = getattr(ts, "first_player_id", None) or getattr(ts, "active_player_id", None)
    order = list(board.player_ids)
    if first in order:
        order = [first] + [pid for pid in order if pid != first]
    rank = {pid: i for i, pid in enumerate(order)}
    candidates.sort(key=lambda pc: (seq.get(pc[1].entity_id, 10 ** 9),
                                    rank.get(pc[1].owning_player_id, 99)))
    live: List[Tuple[Passive, PokemonEntity]] = []
    seen = set()
    next_seq = max(seq.values(), default=0) + 1
    for p, c in candidates:
        seen.add(c.entity_id)
        working = not _non_ability_locked(triples, c) \
            and any(would_lock(p, c, x) for x in in_play)
        if working:
            shielded = _ability_effect_shielded(triples, c)
            for lp, lc in live:
                if lc.owning_player_id != c.owning_player_id and shielded:
                    continue
                if would_lock(lp, lc, c):
                    working = False
                    break
        if working:
            if c.entity_id not in seq:
                seq[c.entity_id] = next_seq
                next_seq += 1
            live.append((p, c))
        else:
            seq.pop(c.entity_id, None)
    for key in [k for k in seq if k not in seen]:
        del seq[key]


def _locks_abilities_of(
    triples: List[Tuple[Passive, BoardEntity, bool]], pokemon: PokemonEntity
) -> bool:
    """Whether any collected passive turns `pokemon`'s Abilities off.

    A shield against the OPPONENT's Ability effects is honoured here:
    Garbotoxin / Initialize turning an Ability off is such an effect, so
    Stealthy Hood (a Tool) and a shielding Ability of the Pokemon's own
    (Hide 'n' Sneak, Mega Clefable ex's Luminous Wing) both defeat an
    opposing Ability lock -- whichever came first. Official Q&A: evolving
    into Mega Clefable ex under a working Initialize, Luminous Wings works.
    A shielding Ability only counts while nothing that is NOT an Ability
    (Path to the Peak, Silent Lab) has switched its carrier off. A lock
    from a Stadium or from the holder's own side is not an opponent's
    Ability and always applies.

    A lock that is itself an Ability counts only while it is LIVE per
    board.ability_lock_seq (see _refresh_ability_lock_seq): silent under a
    non-Ability lock, and silent when an earlier live Ability lock reaches
    its carrier (Klefki vs Flutter Mane).
    """
    shielded = _ability_effect_shielded(triples, pokemon)
    board = board_of(pokemon)
    seq = getattr(board, "ability_lock_seq", None) if board is not None else None
    for passive, carrier, is_ability in triples:
        if not passive.blocks_abilities(pokemon, carrier):
            continue
        if shielded and is_ability \
                and carrier.owning_player_id != pokemon.owning_player_id:
            continue
        if is_ability:
            if _non_ability_locked(triples, carrier):
                continue
            if seq is not None and carrier.entity_id not in seq:
                continue
        return True
    return False


def ability_disabled(board: BoardState, pokemon: PokemonEntity, ability) -> bool:
    """Whether an active passive takes this one `ability` away from
    `pokemon` (Damp). Evaluated on the FILTERED set: Damp is an Ability, so
    a Pokemon whose Abilities are locked contributes no such passive."""
    return any(passive.blocks_ability(pokemon, ability, carrier)
               for passive, carrier in active_passives(board))


def ability_locked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive (Path to the Peak) is disabling `pokemon`'s Abilities.

    Evaluated on the UNFILTERED set: a lock contributed by a Pokemon ability
    is never itself disabled by another lock (Garbotoxin-style recursion is
    out of scope -- Path to the Peak rides a Stadium so this is safe).
    """
    return _locks_abilities_of(_collect_passives(board), pokemon)


# The only out-of-play zones any lock names. Garbotoxin and the XY5 Silent
# Lab both read "in play, in each player's hand, and in each player's discard
# pile" -- neither reaches the Prize cards, the deck or the Lost Zone.
LOCKABLE_OUT_OF_PLAY_AREAS = ("hand", "discard")


def out_of_play_ability_locked(board: BoardState, card: BoardEntity) -> bool:
    """Whether a passive is disabling the Abilities of a card in a hand or a
    discard pile (Garbotoxin).

    The zone check is the card text, not an optimisation: a Jirachi {*} sitting
    in the Prize cards keeps its Ability under Garbotoxin because Garbotoxin
    never mentions the Prizes.

    Evaluated on the UNFILTERED set for the same reason ability_locked is: a
    lock is never switched off by another lock.
    """
    area = card._containing_area_name() if isinstance(card, CardEntity) else None
    if area not in LOCKABLE_OUT_OF_PLAY_AREAS:
        return False
    return any(p.blocks_out_of_play_abilities(card, c)
               for p, c, _ in _collect_passives(board))


def abilities_disabled(board: BoardState, card: BoardEntity) -> bool:
    """Whether `card`'s Abilities are switched off, wherever it is sitting.

    In play, that is the ordinary lock (Path to the Peak). In a hand or a
    discard pile it is the wider one (Garbotoxin). Anywhere else -- the Prize
    cards, the deck, the Lost Zone -- no printed lock reaches it, so nothing
    does.
    """
    area = card._containing_area_name() if isinstance(card, CardEntity) else None
    if area in ("activePokemonArea", "bench"):
        return ability_locked(board, card)
    return out_of_play_ability_locked(board, card)


def _suppressed_special_energy(
    triples: List[Tuple[Passive, BoardEntity, bool]], entity: BoardEntity
) -> bool:
    """Whether `entity` is a Special Energy neutralized by a suppression
    passive (evaluated on the UNFILTERED set, like ability locks)."""
    if not entity.get_attribute(AttrID.IS_SPECIAL_ENERGY):
        return False
    return any(p.suppresses_special_energy(entity, c) for p, c, _ in triples)


def _suppressed_tool(
    triples: List[Tuple[Passive, BoardEntity, bool]], entity: BoardEntity
) -> bool:
    """Whether `entity` is an attached Pokemon Tool neutralized by a
    suppression passive (Tool Jammer), evaluated on the UNFILTERED set."""
    if entity.get_attribute(AttrID.TRAINER_TYPE) != TrainerType.POKEMON_TOOL.value:
        return False
    return any(p.suppresses_tool(entity, c) for p, c, _ in triples)


def active_passives(board: BoardState) -> List[Tuple[Passive, BoardEntity]]:
    """All (passive, carrier) pairs currently switched on by board position.

    Ability passives count only for top-level in-play Pokemon (a tucked
    pre-evolution's ability is off); tool/energy/stadium passives count
    anywhere in an in-play stack. Ability-contributed passives on a Pokemon
    whose own Abilities are locked (Path to the Peak) are excluded, as are
    passives riding a suppressed Special Energy (Temple of Sinnoh).
    """
    triples = _collect_passives(board)

    def blocked(pokemon: PokemonEntity) -> bool:
        return _locks_abilities_of(triples, pokemon)

    # The lock filter asks each lock passive whom it locks; one keyed on a
    # live type (Bide Barricade) would re-enter here through
    # effective_pokemon_types, so the filter runs as a scan too.
    outer = _scanning_passives(board)
    if not outer:
        board._passive_scan_depth = 1
    try:
        return [(p, c) for p, c, is_ability in triples
                if not (is_ability and blocked(c))
                and not _suppressed_special_energy(triples, c)
                and not _suppressed_tool(triples, c)]
    finally:
        if not outer:
            board._passive_scan_depth = 0


def tool_suppressed(board: BoardState, tool: BoardEntity) -> bool:
    """Whether an attached Tool is neutralized (Tool Jammer): gates its
    granted_abilities in PIE_ABILITIES, not just its passive hooks."""
    return _suppressed_tool(_collect_passives(board), tool)


def granted_extra_attacks(board: BoardState, pokemon: PokemonEntity) -> List[Any]:
    """All passive-granted extra attacks for `pokemon`, deduped by ability_id."""
    return [a for _, a in granted_extra_attacks_with_owner(board, pokemon)]


def granted_extra_attacks_with_owner(board: BoardState, pokemon: PokemonEntity) -> List[Any]:
    """granted_extra_attacks as (owner card, attack) pairs, same order and
    dedupe."""
    out: List[Any] = []
    seen = set()
    for passive, carrier in active_passives(board):
        for owner, attack in passive.granted_attacks_with_owner(board, pokemon, carrier) or []:
            if attack.ability_id and attack.ability_id not in seen:
                seen.add(attack.ability_id)
                out.append((owner, attack))
    return out


def _descendants(entity: BoardEntity) -> List[BoardEntity]:
    out: List[BoardEntity] = []
    for child in entity.children:
        out.append(child)
        out.extend(_descendants(child))
    return out


def compute_damage(
    board: BoardState,
    attacker: Optional[BoardEntity],
    target: PokemonEntity,
    base: int,
    is_attack: bool = True,
    apply_modifiers: bool = True,
    ignore_target_effects: bool = False,
    ignore_weakness: bool = False,
    ignore_resistance: bool = False,
    attack_title: Optional[str] = None,
) -> DamageCalc:
    """Runs the full damage pipeline: dealt-modifiers, W/R, taken-modifiers,
    prevention. Returns the finished DamageCalc.

    ignore_weakness (Cramorant's Spit Innocently) skips the Weakness stage but
    keeps Resistance -- distinct from apply_modifiers, which gates both;
    ignore_resistance (Gallade V's Buster Swing) is the exact mirror.
    """
    calc = DamageCalc(board, attacker, target, base,
                      is_attack=is_attack, apply_modifiers=apply_modifiers,
                      ignore_target_effects=ignore_target_effects,
                      attack_title=attack_title)
    if ignore_weakness:
        calc.weakness_applies = False
    if ignore_resistance:
        calc.resistance_applies = False
    passives = active_passives(board)

    if calc.is_attack:
        for passive, carrier in passives:
            passive.modify_damage_dealt(calc, carrier)
        calc.amount = max(0, calc.amount)
        turn_state = getattr(board, "turn_state", None)
        for mod in (turn_state.damage_modifiers if turn_state else []):
            if attacker is None or attacker.owning_player_id != mod.player_id:
                continue
            if mod.requires_subtype and mod.requires_subtype not in subtypes_for(attacker.archetype_id):
                continue
            if mod.source_entity_id and attacker.entity_id != mod.source_entity_id:
                continue
            if mod.attack_title and calc.attack_title != mod.attack_title:
                continue
            if mod.source_predicate is not None and not mod.source_predicate(attacker):
                continue
            if mod.opposing_active_only and not (calc.is_opposing and calc.to_active):
                continue
            calc.amount += mod.amount
        calc.amount = max(0, calc.amount)

    # Wide Lens: a Benched target's hit gets W/R after all (the rules
    # parenthetical was the only thing skipping them).
    if calc.is_attack and not calc.apply_modifiers and attacker is not None             and calc.is_opposing and not calc.to_active             and any(p.applies_bench_modifiers(calc, c) for p, c in passives):
        calc.apply_modifiers = True

    if calc.apply_modifiers and attacker is not None:
        for passive, carrier in passives:
            passive.modify_weakness(calc, carrier)
            passive.modify_resistance(calc, carrier)
        attacker_types = list(attacker.get_attribute(AttrID.POKEMON_TYPES) or [])
        for passive, carrier in passives:
            attacker_types = passive.modify_pokemon_types(attacker_types, attacker, carrier)
        if calc.weakness_applies and any(t in calc.weak_types for t in attacker_types):
            calc.weakness_hit = True
            calc.amount *= calc.weakness_multiplier
        resist_type = target.get_attribute(AttrID.RESISTANCE_TYPES)
        if calc.resistance_applies and resist_type in attacker_types:
            calc.resistance_hit = True
            reduction = (target.get_attribute(AttrID.RESISTANCE_AMOUNT)
                         or RESISTANCE_REDUCTION)
            calc.amount = max(0, calc.amount - reduction)

    for passive, carrier in passives:
        if calc.ignore_target_effects and carrier_pokemon(carrier) is calc.target:
            continue
        passive.modify_damage_taken(calc, carrier)
    calc.amount = max(0, calc.amount)

    for passive, carrier in passives:
        if calc.ignore_target_effects and carrier_pokemon(carrier) is calc.target:
            continue
        if passive.prevents_damage(calc, carrier):
            calc.prevented = True
            calc.amount = 0
            break
    return calc


def effective_attack_cost(
    board: BoardState, pokemon: PokemonEntity, cost: Dict[str, int]
) -> Dict[str, int]:
    """An attack's cost after cost-modifying passives (e.g. Excited Heart)."""
    for passive, carrier in active_passives(board):
        cost = passive.modify_attack_cost(dict(cost), pokemon, carrier, board)
    return cost


def effective_retreat_cost(board: BoardState, pokemon: PokemonEntity) -> int:
    """A Pokemon's retreat cost after cost-modifying passives (Air Balloon's -2)."""
    cost = int(pokemon.get_attribute(AttrID.RETREAT_COST) or 0)
    for passive, carrier in active_passives(board):
        cost = passive.modify_retreat_cost(cost, pokemon, carrier, board)
    return max(0, cost)


def effective_max_hp(board: BoardState, pokemon: PokemonEntity) -> int:
    """Printed max HP plus every max-HP bonus riding the Pokemon's stack;
    passives sharing a stacking_key count once (Abomasnow)."""
    printed = pokemon.attribute_originals.get(
        AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0)
    )
    bonus = 0
    seen_keys: Set[str] = set()
    for passive, carrier in active_passives(board):
        key = passive.stacking_key
        if key is not None and key in seen_keys:
            continue
        gained = passive.max_hp_bonus(pokemon, carrier)
        if gained and key is not None:
            seen_keys.add(key)
        bonus += gained
    return printed + bonus


def attack_effects_blocked(board: BoardState, target: PokemonEntity,
                           source: Optional[PokemonEntity] = None) -> bool:
    """Whether a passive shields `target` from opposing attack effects.

    `source` is the attacking Pokemon where the caller knows it; a shield
    that reads the attacker (Alolan Persian-GX's Smug Face) needs it, and
    the rest ignore it.
    """
    return any(
        passive.blocks_attack_effects(target, carrier, source)
        for passive, carrier in active_passives(board)
    )


def retreat_blocked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive forbids `pokemon` from retreating."""
    return any(
        passive.blocks_retreat(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def attacking_blocked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a continuous passive stops this Pokemon attacking at all."""
    return any(
        passive.blocks_attacking(pokemon, carrier, board)
        for passive, carrier in active_passives(board)
    )


def can_attack_first_turn(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive lets `pokemon` attack on the going-first turn 1."""
    return any(
        passive.attacks_first_turn(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def can_attack_despite_conditions(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive lets `pokemon` attack while Asleep/Paralyzed."""
    return any(
        passive.attacks_despite_conditions(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def mega_evolution_ends_turn(board: BoardState, pokemon: PokemonEntity) -> bool:
    """The Mega Evolution rule: "When 1 of your Pokemon becomes a Mega
    Evolution Pokemon, your turn ends" -- unless a passive on that Pokemon
    (a Spirit Link) waives it. Asked with the Mega already on top."""
    if "MEGA" not in subtypes_for(pokemon.archetype_id):
        return False
    return not any(passive.mega_evolution_keeps_turn(pokemon, carrier)
                   for passive, carrier in active_passives(board))


def sleep_checkup_coin_count(board: BoardState, pokemon: PokemonEntity) -> int:
    """Coins `pokemon` flips to wake up: 1, or the largest figure a passive
    names (Slumbering Forest's 2)."""
    coins = 1
    for passive, carrier in active_passives(board):
        coins = max(coins, passive.sleep_checkup_coins(pokemon, carrier))
    return coins


def supporter_play_limit(board: BoardState, player_id: str) -> int:
    """Supporter plays allowed to `player_id` this turn: 1, or the largest
    figure a passive names (Dual Brains)."""
    limit = 1
    for passive, carrier in active_passives(board):
        limit = max(limit, passive.supporter_play_limit(player_id, carrier))
    return limit


def can_retreat_despite_conditions(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive lets `pokemon` retreat while Asleep/Paralyzed."""
    return any(
        passive.retreats_despite_conditions(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def discard_destination_for(board: BoardState, card: BoardEntity) -> Optional[str]:
    """First non-None area a passive sends `card` to instead of the discard
    pile when it leaves play (U-Turn Board's "into your hand"), or None."""
    for passive, carrier in active_passives(board):
        dest = passive.discard_destination(card, carrier)
        if dest is not None:
            return dest
    return None


def conditions_blocked(board: BoardState, target: PokemonEntity, condition: Any) -> bool:
    """Whether a passive shields `target` from the given Special Condition."""
    return any(
        passive.blocks_special_conditions(target, condition, carrier)
        for passive, carrier in active_passives(board)
    )


def healing_blocked(board: BoardState, target: PokemonEntity) -> bool:
    """Whether a passive prevents healing damage from `target`."""
    return any(
        passive.prevents_healing(target, carrier)
        for passive, carrier in active_passives(board)
    )


def effective_heal_amount(board: BoardState, target: PokemonEntity, amount: int) -> int:
    """Heal amount after stadium/passive multipliers (Legendary Ocean Trench);
    passives sharing a stacking_key count once."""
    if amount <= 0:
        return 0
    seen_keys: Set[str] = set()
    multiplier = 1
    for passive, carrier in active_passives(board):
        key = passive.stacking_key
        if key is not None and key in seen_keys:
            continue
        gained = passive.heal_multiplier(target, carrier)
        if gained != 1:
            if key is not None:
                seen_keys.add(key)
            multiplier *= gained
    return amount * multiplier


def trainer_targeting_blocked(board: BoardState, target: BoardEntity) -> bool:
    """Whether Item and Supporter cards cannot touch `target` at all."""
    return any(
        passive.blocks_trainer_targeting(target, carrier)
        for passive, carrier in active_passives(board)
    )


def ability_effects_blocked(board: BoardState, target: PokemonEntity) -> bool:
    """Whether a passive shields `target` from opposing Ability effects."""
    return any(
        passive.blocks_ability_effects(target, carrier)
        for passive, carrier in active_passives(board)
    )


def damage_counters_blocked(board: BoardState, target: PokemonEntity) -> bool:
    """Whether a passive prevents placing damage counters on `target`."""
    return any(
        passive.blocks_damage_counters(target, carrier)
        for passive, carrier in active_passives(board)
    )


def moving_damage_counters_blocked(board: BoardState) -> bool:
    """Whether a passive forbids moving damage counters between Pokémon."""
    return any(
        passive.blocks_moving_damage_counters(carrier)
        for passive, carrier in active_passives(board)
    )


def putting_into_play_blocked(board: BoardState, player_id: str, card: BoardEntity) -> bool:
    """Whether a continuous passive forbids `player_id` putting `card` into
    play (Eternal Zone and a non-Darkness Pokemon)."""
    return any(
        passive.blocks_putting_into_play(card, player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def trainer_play_blocked(board: BoardState, player_id: str, card: BoardEntity) -> bool:
    """Whether a continuous passive forbids playing `card` from hand."""
    return any(
        passive.blocks_trainer_play(card, player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def discard_blocked(board: BoardState, card: BoardEntity) -> bool:
    """Whether a passive protects `card` from an opponent-caused discard."""
    return any(
        passive.blocks_discard(card, carrier)
        for passive, carrier in active_passives(board)
    )


def discard_recovery_blocked(board: BoardState, player_id: str) -> bool:
    """Whether a passive keeps `player_id`'s Abilities/Trainers from
    returning cards from their discard pile to their hand."""
    return any(
        passive.blocks_discard_recovery(player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def tool_attach_blocked(board: BoardState, player_id: str) -> bool:
    """Whether a passive keeps `player_id` from attaching Tools from hand."""
    return any(
        passive.blocks_tool_attach(player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def effective_turn_draw(board: BoardState, player_id: str) -> int:
    """How many cards `player_id` draws at the start of their turn."""
    count = 1
    for passive, carrier in active_passives(board):
        count = passive.turn_draw_count(player_id, count, carrier)
    return max(0, count)


def player_attack_effects_blocked(board: BoardState, player_id: str) -> bool:
    """Whether a passive shields `player_id` (and their hand) from the
    effects of opposing attacks (Bodyguard)."""
    return any(
        passive.blocks_player_attack_effects(player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def trainer_effects_blocked(board: BoardState, affected_player_id: str,
                            trainer_card: BoardEntity,
                            affected_entity: Optional[BoardEntity] = None) -> bool:
    """Whether a passive shields `affected_player_id` from `trainer_card`'s
    effects (Dew Guard); callers scope this to cross-player effects."""
    trainer_type = trainer_card.get_attribute(AttrID.TRAINER_TYPE)
    return any(
        passive.blocks_trainer_effects(
            affected_player_id, trainer_card, trainer_type, carrier,
            affected_entity=affected_entity, board=board)
        for passive, carrier in active_passives(board)
    )


def supporter_effect_replacement(board: BoardState, card: BoardEntity,
                                 player_id: str) -> Optional[Any]:
    """First replacement coroutine a passive offers for this Supporter play
    (Shifty Substitution), or None."""
    for passive, carrier in active_passives(board):
        replacement = passive.replace_supporter_effect(card, player_id, carrier)
        if replacement is not None:
            return replacement
    return None


def active_to_bench_counters(board: BoardState, pokemon: PokemonEntity) -> int:
    """Damage counters for an Active that moved to its owner's Bench during
    the owner's turn (Spikemuth); callers gate on whose turn it is."""
    return sum(
        passive.counters_on_active_to_bench(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def evolve_heal_amount(board: BoardState, evolved: PokemonEntity,
                       pre_evolution: BoardEntity, player_id: str) -> int:
    """Damage healed from a Pokemon just evolved from hand (Wyndon Stadium)."""
    return sum(
        passive.heal_on_evolve(evolved, pre_evolution, player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def attack_coin_reroll_offered(
    board: BoardState, player_id: str, attacker: Optional[BoardEntity] = None
) -> bool:
    """Whether a passive lets `player_id` re-flip attack coins (Glimwood Tangle)."""
    return any(
        passive.offers_attack_coin_reroll(player_id, carrier, attacker)
        for passive, carrier in active_passives(board)
    )


def energy_attach_taxer(board: BoardState, attaching_player_id: str,
                        energy: BoardEntity, target: PokemonEntity) -> Optional[BoardEntity]:
    """The carrier taxing this manual energy attach (Slimy Room), or None."""
    for passive, carrier in active_passives(board):
        if passive.taxes_energy_attach(attaching_player_id, energy, target, carrier):
            return carrier
    return None


def retreat_energy_destination(board: BoardState, pokemon: PokemonEntity,
                               energy: BoardEntity) -> Optional[str]:
    """First non-None area a passive redirects a retreat-cost energy to
    (Skaters' Park), or None for the normal discard."""
    for passive, carrier in active_passives(board):
        dest = passive.retreat_cost_destination(pokemon, energy, carrier)
        if dest is not None:
            return dest
    return None


def evolution_blocked(board: BoardState, player_id: str, target: PokemonEntity) -> bool:
    """Whether a passive forbids `player_id` evolving `target` (Dracovish)."""
    return any(
        passive.blocks_evolution(player_id, target, carrier)
        for passive, carrier in active_passives(board)
    )


def can_evolve_early(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive exempts `pokemon` from the evolution turn gates."""
    return any(
        passive.may_evolve_early(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def can_evolve_same_turn(
    board: BoardState, pokemon: PokemonEntity, evolution_card: BoardEntity
) -> bool:
    """Whether a passive lets `pokemon` evolve the turn it was played
    (still forbidden on either player's first turn)."""
    return any(
        passive.may_evolve_same_turn(pokemon, carrier, evolution_card)
        for passive, carrier in active_passives(board)
    )


def can_evolve_onto(
    board: BoardState, pokemon: PokemonEntity, evolution_card: BoardEntity
) -> bool:
    """Whether a passive lets `evolution_card` evolve onto `pokemon` despite
    a name mismatch (Rainbow DNA)."""
    return any(
        passive.may_be_evolved_into(pokemon, carrier, evolution_card)
        for passive, carrier in active_passives(board)
    )


def burn_recovery_blocked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive skips the Burn recovery flip for `pokemon`."""
    return any(
        passive.blocks_burn_recovery(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def special_energy_suppressed(board: BoardState, energy: BoardEntity) -> bool:
    """Whether `energy` is a Special Energy neutralized by a passive."""
    return _suppressed_special_energy(_collect_passives(board), energy)


def effective_pokemon_types(board: BoardState, pokemon: BoardEntity) -> List[Any]:
    """A Pokemon's live type list after type-rewriting passives (Chromashift)."""
    types = list(pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
    if _scanning_passives(board):
        # Asked from inside a passive scan (a lock passive's own type
        # test): the printed types, or the scan would start over.
        return types
    for passive, carrier in active_passives(board):
        types = passive.modify_pokemon_types(types, pokemon, carrier)
    return types


def energy_removal_blocked(board: BoardState, mover_player_id: str,
                           card: BoardEntity) -> bool:
    """Whether a passive keeps this attached Energy from being moved to
    hand/deck/discard by `mover_player_id`'s trainer effect (Brazen Tail)."""
    return any(
        passive.blocks_energy_removal(card, mover_player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def energy_provided_options(board: Optional[BoardState], energy: BoardEntity) -> List[List[int]]:
    """An energy card's provided-type options after suppression (a suppressed
    Special Energy provides only Colorless) and modify_energy_provided hooks."""
    info = energy.get_attribute(AttrID.ENERGY_INFO) or {}
    options = [list(option) for option in info.get("options", [])]
    if board is None:
        return options
    if special_energy_suppressed(board, energy):
        options = [[PokemonTypes.COLORLESS.value]]
    holder = carrier_pokemon(energy)
    for passive, carrier in active_passives(board):
        # A Special Energy's own passive (Rainbow, Unit, Counter, Beast...)
        # rewrites what THAT card provides and nothing else -- without this
        # gate one Rainbow Energy in play made every attached Energy on both
        # sides provide every type. Pokemon-carried rewrites (Charizard
        # PGO's doubling) still reach every Energy they name.
        if isinstance(carrier, EnergyEntity) and carrier is not energy:
            continue
        options = passive.modify_energy_provided(options, energy, holder, board)
    return options


def effective_bench_capacity(board: BoardState, player_id: str) -> int:
    """Bench size for `player_id` after capacity passives; the smallest
    override wins (Collapsed Stadium caps an Eternatus board at 4)."""
    values = [
        v for passive, carrier in active_passives(board)
        for v in [passive.bench_capacity(player_id, carrier)] if v is not None
    ]
    return max(1, min(values)) if values else BENCH_SLOT_COUNT


def bench_space(board: BoardState, player_id: str) -> int:
    """Free Bench slots for `player_id` under the live capacity (Sky Field's
    8, Collapsed Stadium's 4) -- the number every "put onto your Bench"
    search may take. Never the flat BENCH_CAPACITY constant."""
    bench = board.find_player_area(player_id, "bench")
    if bench is None:
        return 0
    return max(0, effective_bench_capacity(board, player_id) - len(bench.children))


def player_visualizations(board: BoardState, player_id: str) -> List[Dict[str, Any]]:
    """Every active passive's status rows for `player_id`, in passive order.

    Derived state, not stored: the caller replaces the player's attr 200370
    with whatever this returns, so a Stadium leaving play removes its rows
    without anyone having to remember to clear them."""
    rows: List[Dict[str, Any]] = []
    for passive, carrier in active_passives(board):
        rows.extend(passive.player_visualizations(player_id, carrier) or [])
    return rows


def coin_flips_forced_tails(board: BoardState, flipper_id: str) -> bool:
    """Whether a passive turns every coin `flipper_id` flips during their
    turn into tails (Contrary). Applied after Will's chosen result -- a
    heads chosen by Will is still a coin the opponent flipped (ruling)."""
    turn_state = getattr(board, "turn_state", None)
    if turn_state is not None and turn_state.active_player_id != flipper_id:
        return False
    return any(passive.forces_coin_tails(flipper_id, carrier)
               for passive, carrier in active_passives(board))


def tool_slots_free(board: Optional[BoardState], pokemon: PokemonEntity) -> int:
    """Open Pokemon Tool slots on `pokemon` (default capacity 1; the highest
    tool_capacity passive wins)."""
    capacity = 1
    if board is not None:
        for passive, carrier in active_passives(board):
            capacity = max(capacity, passive.tool_capacity(pokemon, carrier))
    attached = sum(
        1 for child in pokemon.children
        if child.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value
    )
    return capacity - attached
