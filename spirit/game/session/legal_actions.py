"""Legal-action computation for the main turn loop.

Builds the targetMap of a SelectionWithTargetsAndActionsRequired offer; the
client highlights exactly those entities (it does no legality checks itself).
"""

import logging
import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

from spirit.game.attributes import (
    AttrID,
    CLIENT_SPECIAL_CONDITION_NAMES,
    PokemonStage,
    PokemonTypes,
    POKEMON_TYPES_BY_CLIENT_NAME,
    SpecialConditions,
    TrainerType,
)
from spirit.game.data_utils import (ABILITIES_BY_ID, Activations, def_for,
                                    unplayable_from_hand_now,
                                    searches_deck)
from spirit.game.models.board import (
    BoardState,
    EnergyEntity,
    PokemonEntity,
    TrainerEntity,
)
from .constants import (
    PROMPT_RETREAT_COST,
    PROMPT_RETREAT_NEW_ACTIVE,
    SelectionKind,
)
from .passives import (
    putting_into_play_blocked,
    granted_extra_attacks_with_owner,
    ability_locked,
    abilities_disabled,
    attack_effects_blocked,
    tool_attach_blocked,
    attacking_blocked,
    out_of_play_ability_locked,
    can_attack_despite_conditions,
    can_attack_first_turn,
    can_retreat_despite_conditions,
    supporter_play_limit,
    can_evolve_early,
    can_evolve_onto,
    can_evolve_same_turn,
    effective_attack_cost,
    effective_bench_capacity,
    effective_retreat_cost,
    energy_provided_options,
    evolution_blocked,
    retreat_blocked,
    tool_slots_free,
    trainer_play_blocked,
)


# Semantic action names from the client's Actions enum / SelectableActionUtil.
ACTION_PLAY_POKEMON = "DefaultPokemonPlayAbility"
ACTION_EVOLVE = "EvolvePokemonPlayAbility"
ACTION_PLAY_ENERGY = "DefaultEnergyPlayAbility"
ACTION_USE_TRAINER = "UseTrainerCard"
ACTION_PLAY_STADIUM = "DefaultStadiumPlayAbility"
ACTION_USE_ABILITY = "UsePokemonAbility"
ACTION_USE_ATTACK = "UsePokemonAttack"
ACTION_RETREAT = "BaseRetreat"
# No dedicated tool member exists in the client's Actions enum; the string is
# free-form (only the action-panel icon lookup reads it) and the drop target
# comes from the target node's validTargets, exactly like energy.
ACTION_ATTACH_TOOL = "DefaultToolPlayAbility"

# Conditions that stop the Active from attacking or retreating.
_IMMOBILIZING_CONDITIONS = {
    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP],
    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.PARALYZED],
}

# ActionsNode Kind: "Ability" (j.V) auto-resolves plays; "AbilitySelection" (K.O) opens the ability panel.
SELECTION_TYPE_PLAY = SelectionKind.ABILITY.value
SELECTION_TYPE_PANEL = SelectionKind.ABILITY_SELECTION.value

# Energy cost types that any energy card can pay.
_WILDCARD_COST_TYPES = (PokemonTypes.NO_COLOR.value, PokemonTypes.COLORLESS.value)

_ACTION_ID_NAMESPACE = uuid.UUID("f6c1b1de-5e1a-4b52-9c40-1d1c4e6a7b0d")

# Sentinel lock horizon: stays locked until the Pokemon leaves the Active spot.
LOCK_UNTIL_LEAVES_ACTIVE = 10 ** 9


def action_id_for(entity_id: str, verb: str) -> str:
    """Deterministic GUID action ID (must be a GUID: the client runs new Guid(id))."""
    return str(uuid.uuid5(_ACTION_ID_NAMESPACE, f"{entity_id}:{verb}"))


@dataclass
class TurnState:
    """Per-game turn bookkeeping consumed by the legality rules."""

    turn_number: int = 0
    # Who goes first (set once the opening coin is decided): breaks ties
    # between Ability locks that start working in the same pass.
    first_player_id: Optional[str] = None
    active_player_id: Optional[str] = None
    supporter_played: bool = False
    # How many Supporters the turn player has played; the limit is 1 unless
    # a passive raises it (Magnezone's Dual Brains), so both are kept.
    supporter_plays: int = 0
    # A player may play only 1 Stadium per turn, the same way they may
    # play only 1 Supporter. Set even when the Stadium never reaches the
    # board (Chaotic Swell sweeps it): playing it is what spends the turn's
    # allowance, not it staying in play.
    stadium_played: bool = False
    energy_attached: bool = False
    retreated: bool = False
    # entity_id -> turn number it entered play (or last evolved). Entities
    # placed during setup are absent and default to turn 0.
    entered_play_turn: Dict[str, int] = field(default_factory=dict)
    # (entity_id, ability_id) pairs used this turn (once-per-turn abilities).
    used_abilities: Set[Tuple[str, str]] = field(default_factory=set)
    # Ability names used this turn that are "1 per turn" shared across copies
    # (Dark Asset, Flower Selecting, Dragon's Hoard).
    used_named_abilities: Set[str] = field(default_factory=set)
    # Players who already used their once-per-game VSTAR Power.
    vstar_used: Set[str] = field(default_factory=set)
    # Players who already used their once-per-game GX attack.
    gx_used: Set[str] = field(default_factory=set)
    # player_id -> [predicate(pokemon)]: Pokemon that may use a GX attack
    # THIS turn even though the player already used theirs (Misty &
    # Lorelei's "your [W] Pokemon"). Cleared every begin_turn.
    gx_reuse: Dict[str, List[Any]] = field(default_factory=dict)
    # "For the rest of this game, your opponent can't use any GX attacks"
    # (Latios-GX's Clear Vision-GX): [{"player_id", "source"}], source being
    # the Pokemon that used the attack. Checked per attacker, so a Pokemon
    # shielded from that source's attack effects (Keldeo-GX's Pure Heart vs
    # a Pokemon-GX) is not bound. An effect of an attack on a player, so
    # Pokemon Ranger removes it (the ledger lists it); it never expires.
    gx_blocks: List[Dict[str, Any]] = field(default_factory=list)
    # (entity_id, ability_id) -> last turn number the attack stays locked
    # ("during your next turn, this Pokemon can't use ...").
    attack_locks: Dict[Tuple[str, str], int] = field(default_factory=dict)
    # entity_id -> last turn number retreat stays locked ("the Defending
    # Pokemon can't retreat"); LOCK_UNTIL_LEAVES_ACTIVE = until it leaves.
    retreat_locks: Dict[str, int] = field(default_factory=dict)
    # Turn-scoped attacker-side damage boosts (Power Tablet); pruned by
    # expires_after_turn each begin_turn (None = this turn only).
    damage_modifiers: List[Any] = field(default_factory=list)
    # --- two-turn history ledgers, rotated this-turn -> last-turn ---
    # (archetype_id, display_name, trainer_type) per trainer/stadium played.
    trainers_played: List[Tuple[str, str, int]] = field(default_factory=list)
    # (entity_id, archetype_id, attack_title) per declared attack.
    attacks_used: List[Tuple[str, str, str]] = field(default_factory=list)
    # victim owner player_id -> [{archetype_id, subtypes}] for attack KOs.
    kos_by_attack: Dict[str, List[Dict[str, Any]]] = field(default_factory=dict)
    # entity_id -> damage dealt to it by the other side this turn.
    damage_taken: Dict[str, int] = field(default_factory=dict)
    # player_id -> prize cards taken this turn.
    prizes_taken: Dict[str, int] = field(default_factory=dict)
    retreated_entities: Set[str] = field(default_factory=set)
    healed_entities: Set[str] = field(default_factory=set)
    turn_draw_entity_ids: Set[str] = field(default_factory=set)
    trainers_played_last_turn: List[Tuple[str, str, int]] = field(default_factory=list)
    attacks_used_last_turn: List[Tuple[str, str, str]] = field(default_factory=list)
    kos_by_attack_last_turn: Dict[str, List[Dict[str, Any]]] = field(default_factory=dict)
    # Every knockout, whatever caused it, keyed by the owner of the Pokemon
    # that was lost. "Knocked Out during your opponent's last turn" counts
    # poison, damage counters and Trainers too, which kos_by_attack does not.
    kos_suffered: Dict[str, List[Dict[str, Any]]] = field(default_factory=dict)
    kos_suffered_last_turn: Dict[str, List[Dict[str, Any]]] = field(default_factory=dict)
    damage_taken_last_turn: Dict[str, int] = field(default_factory=dict)
    prizes_taken_last_turn: Dict[str, int] = field(default_factory=dict)
    retreated_entities_last_turn: Set[str] = field(default_factory=set)
    healed_entities_last_turn: Set[str] = field(default_factory=set)
    turn_draw_entity_ids_last_turn: Set[str] = field(default_factory=set)
    # entity_id -> turn it last moved into the Active spot (persistent stamp).
    became_active_turn: Dict[str, int] = field(default_factory=dict)
    # player_id -> [(card_predicate, expires_after_turn)] play restrictions
    # ("your opponent can't play Item cards during their next turn"); a None
    # expiry holds until cleared.
    play_locks: Dict[str, List[Tuple[Any, Optional[int]]]] = field(default_factory=dict)
    # entity_id -> last turn number energy may not be attached to it (Masquerain).
    attach_restrictions: Dict[str, int] = field(default_factory=dict)
    # Entities whose ON_MOVE_TO_ACTIVE trigger already fired this turn.
    on_move_to_active_fired: Set[str] = field(default_factory=set)
    # entity_id -> the turn at whose END this Pokemon is Knocked Out
    # ("At the end of your opponent's next turn, the Defending Pokemon will
    # be Knocked Out" -- Pale Moon-GX). Not a per-turn ledger: entries sit
    # here until they fire or the Pokemon leaves play.
    scheduled_knockouts: Dict[str, int] = field(default_factory=dict)
    # Pokemon that were devolved this turn: "(That Pokemon can't evolve this
    # turn.)" Kept apart from entered_play_turn, which means "came into play
    # this turn" and is read by cards asking whether this Pokemon EVOLVED
    # this turn -- a devolved one did not.
    devolved_this_turn: Set[str] = field(default_factory=set)
    # Whether the turn player used their once-per-turn attack-coin re-flip
    # (Glimwood Tangle); only actually re-flipping consumes it.
    attack_coin_reroll_used: bool = False
    # Will: "the next time you flip any number of coins ... this turn, choose
    # heads or tails for the first coin flip". True = heads, None = nothing
    # chosen; the first flip of the turn after it is set consumes it.
    forced_first_flip: Optional[bool] = None
    # entity_id -> (through_turn, flip_title): a Smokescreen-family check --
    # this entity must flip a coin to attack, tails cancels the attack.
    attack_flip_checks: Dict[str, Tuple[int, str]] = field(default_factory=dict)
    # Entities whose attacks ignore effects on the opponent's Active THIS turn
    # (Phoebe); cleared every begin_turn.
    ignore_target_effects_entities: Set[str] = field(default_factory=set)
    # player_id -> attack titles that player declared on THEIR previous turn
    # ("If 1 of your Pokemon used Yoga Loop during your last turn...").
    attack_titles_prev_turn_by_player: Dict[str, List[str]] = field(default_factory=dict)
    # This-turn bonus-prize watches (Sky Seal Stone's Star Order):
    # {player_id, attacker_predicate, target_predicate, prizes}; consulted by
    # resolve_knockouts on attack-damage KOs, cleared every begin_turn.
    extra_prize_watchers: List[Dict[str, Any]] = field(default_factory=list)
    # After a keep-turn attack (Festival Lead / Fluffy Barrage), Yes on the
    # second-attack prompt stamps the attacker here so the next main offer
    # auto-selects it and opens the attack panel.
    auto_select_attack_entity_id: Optional[str] = None
    # The extra attack now on offer is Festival Lead's, which repeats
    # only an attack the Pokemon HAS: attacks lent by a Tool or an
    # Energy drop off the panel for it. See Passive.extra_attack_printed_only.
    extra_attack_printed_only: bool = False
    # Which entries of the effect stores above an ATTACK put there
    # (Pokemon Ranger: "Remove all effects of attacks on each player and each
    # of their Pokemon"). Filled by resolve_attack from a before/after
    # snapshot, so every writer -- helper or card script -- is caught;
    # entries an Ability or Trainer made are never listed and so survive.
    # (store_name, key) for dict stores, (store_name, object) for lists.
    attack_effects: List[Tuple[str, Any]] = field(default_factory=list)

    def pokemon_lost_last_turn(self, player_id: str) -> List[Dict[str, Any]]:
        """"if any of your Pokemon were Knocked Out during your opponent's
        last turn" -- every knockout, whatever caused it.

        The one place that decides which ledger that sentence means. Text
        that instead says "by damage from an opponent's attack" (Dhelmise V,
        Kangaskhan) reads kos_by_attack_last_turn directly.
        """
        return (self.kos_suffered_last_turn or {}).get(player_id, [])

    def begin_turn(self, player_id: str, board: Optional[Any] = None):
        """Advances to the next turn, resets the once-per-turn flags, rotates
        the two-turn history, and prunes expired turn-scoped effects.

        A second turn in a row for the same player (Dialga-GX's Timeless GX)
        leaves the knockout ledgers where they are. The opponent has not had a
        turn in between, so "Knocked Out during your opponent's last turn"
        still means the turn it meant a moment ago, and Dance of Tribute /
        Flip the Script stay usable through the extra turn.
        """
        extra_turn = bool(self.active_player_id) and self.active_player_id == player_id
        if self.active_player_id:
            self.attack_titles_prev_turn_by_player[self.active_player_id] = [
                title for _, _, title in self.attacks_used
            ]
        self.turn_number += 1
        self.active_player_id = player_id
        self.supporter_played = False
        self.supporter_plays = 0
        self.stadium_played = False
        self.energy_attached = False
        self.retreated = False
        self.used_abilities = set()
        self.used_named_abilities = set()
        self.damage_modifiers = [
            m for m in self.damage_modifiers
            if getattr(m, "permanent", False)
            or (getattr(m, "expires_after_turn", None) is not None
                and m.expires_after_turn >= self.turn_number)
        ]
        self.trainers_played_last_turn = self.trainers_played
        self.trainers_played = []
        self.attacks_used_last_turn = self.attacks_used
        self.attacks_used = []
        if not extra_turn:
            self.kos_by_attack_last_turn = self.kos_by_attack
            self.kos_by_attack = {}
            self.kos_suffered_last_turn = self.kos_suffered
            self.kos_suffered = {}
        self.damage_taken_last_turn = self.damage_taken
        self.damage_taken = {}
        self.prizes_taken_last_turn = self.prizes_taken
        self.prizes_taken = {}
        self.retreated_entities_last_turn = self.retreated_entities
        self.retreated_entities = set()
        self.healed_entities_last_turn = self.healed_entities
        self.healed_entities = set()
        self.turn_draw_entity_ids_last_turn = self.turn_draw_entity_ids
        self.turn_draw_entity_ids = set()
        self.on_move_to_active_fired = set()
        self.devolved_this_turn = set()
        self.attack_coin_reroll_used = False
        self.forced_first_flip = None
        self.gx_reuse = {}
        self.play_locks = {
            pid: kept for pid, locks in self.play_locks.items()
            if (kept := [(p, exp) for p, exp in locks
                         if exp is None or exp >= self.turn_number])
        }
        self.attach_restrictions = {
            eid: exp for eid, exp in self.attach_restrictions.items()
            if exp >= self.turn_number
        }
        self.attack_flip_checks = {
            eid: entry for eid, entry in self.attack_flip_checks.items()
            if entry[0] >= self.turn_number
        }
        self.ignore_target_effects_entities = set()
        # "For the rest of this game" watches (Altered Creation-GX) survive
        # the turn rollover; the rest are this-turn only.
        self.extra_prize_watchers = [
            w for w in self.extra_prize_watchers if w.get("permanent")
        ]
        self.auto_select_attack_entity_id = None
        self.extra_attack_printed_only = False
        if board is not None:
            board.temporary_passives = [
                tp for tp in (getattr(board, "temporary_passives", None) or [])
                if tp.expires_after_turn is None
                or tp.expires_after_turn >= self.turn_number
            ]
        self._prune_attack_effects()

    # ------------------------------------------------------------------
    # "Effects of attacks" ledger (Pokemon Ranger)
    # ------------------------------------------------------------------

    _DICT_EFFECT_STORES = ("attack_locks", "retreat_locks", "attach_restrictions",
                           "attack_flip_checks", "scheduled_knockouts")
    _LIST_EFFECT_STORES = ("damage_modifiers", "extra_prize_watchers", "gx_blocks")

    def _prune_attack_effects(self) -> None:
        """Forget ledger entries whose store entry already expired, so a
        later same-keyed entry made by an Ability is not mistaken for it."""
        def alive(name, key) -> bool:
            if name in self._DICT_EFFECT_STORES:
                store = getattr(self, name)
                if key not in store:
                    return False
                # These stores keep expired entries around; an entry whose
                # "through turn" has passed is spent.
                value = store[key]
                through = value[0] if isinstance(value, tuple) else value
                return not isinstance(through, int) or through >= self.turn_number
            if name in self._LIST_EFFECT_STORES:
                return any(x is key for x in getattr(self, name))
            if name == "play_locks":
                return any(x is key for locks in self.play_locks.values() for x in locks)
            return False
        self.attack_effects = [(n, k) for n, k in self.attack_effects if alive(n, k)]

    def snapshot_effect_stores(self, board: Optional[Any] = None) -> Dict[str, Any]:
        """What the effect stores hold right now, for record_attack_effects."""
        snap: Dict[str, Any] = {}
        for name in self._DICT_EFFECT_STORES:
            snap[name] = dict(getattr(self, name))
        for name in self._LIST_EFFECT_STORES:
            snap[name] = {id(x) for x in getattr(self, name)}
        snap["play_locks"] = {id(entry) for locks in self.play_locks.values()
                              for entry in locks}
        snap["temporary_passives"] = {
            id(tp) for tp in (getattr(board, "temporary_passives", None) or [])}
        return snap

    def record_attack_effects(self, snapshot: Dict[str, Any],
                              board: Optional[Any] = None) -> None:
        """Everything the stores gained (or changed) since `snapshot` was an
        attack's doing: list it so Pokemon Ranger can take it away."""
        for name in self._DICT_EFFECT_STORES:
            before = snapshot[name]
            for key, value in getattr(self, name).items():
                if key not in before or before[key] != value:
                    self.attack_effects.append((name, key))
        for name in self._LIST_EFFECT_STORES:
            for obj in getattr(self, name):
                if id(obj) not in snapshot[name]:
                    self.attack_effects.append((name, obj))
        for locks in self.play_locks.values():
            for entry in locks:
                if id(entry) not in snapshot["play_locks"]:
                    self.attack_effects.append(("play_locks", entry))
        for tp in (getattr(board, "temporary_passives", None) or []):
            if id(tp) not in snapshot["temporary_passives"]:
                tp.from_attack = True

    def clear_attack_effects(self, board: Optional[Any] = None) -> int:
        """Pokemon Ranger: drops every listed attack effect from the stores
        (Special Conditions and damage are not effects of attacks and stay).
        Returns how many entries went."""
        removed = 0
        for name, key in self.attack_effects:
            if name in self._DICT_EFFECT_STORES:
                if key in getattr(self, name):
                    del getattr(self, name)[key]
                    removed += 1
            elif name in self._LIST_EFFECT_STORES:
                store = getattr(self, name)
                if any(x is key for x in store):
                    setattr(self, name, [x for x in store if x is not key])
                    removed += 1
            elif name == "play_locks":
                for pid, locks in list(self.play_locks.items()):
                    if any(x is key for x in locks):
                        self.play_locks[pid] = [x for x in locks if x is not key]
                        removed += 1
        self.attack_effects = []
        if board is not None:
            kept = [tp for tp in (getattr(board, "temporary_passives", None) or [])
                    if not getattr(tp, "from_attack", False)]
            removed += len(board.temporary_passives) - len(kept)
            board.temporary_passives = kept
        return removed

    def gx_available(self, player_id: str, pokemon: Any,
                     board: Optional[Any] = None) -> bool:
        """May `pokemon` use a GX attack now: no Clear Vision-GX binds it
        (a shield against its source's attack effects lifts that), and the
        player's once-per-game use is unspent -- or a this-turn allowance
        (Misty & Lorelei) names this Pokemon. The allowance does not get
        past Clear Vision: it forgives a spent GX attack, not a ban."""
        for block in self.gx_blocks:
            if block.get("player_id") != player_id:
                continue
            if board is not None and pokemon is not None and attack_effects_blocked(
                    board, pokemon, block.get("source")):
                continue
            return False
        if player_id not in self.gx_used:
            return True
        return any(pred(pokemon) for pred in self.gx_reuse.get(player_id, []))

    def allow_gx_reuse(self, player_id: str, predicate) -> None:
        self.gx_reuse.setdefault(player_id, []).append(predicate)

    def block_gx_attacks(self, player_id: str, source: Any) -> None:
        """Clear Vision-GX: `player_id` can't use GX attacks for the rest of
        the game (per-attacker shields against `source` excepted)."""
        self.gx_blocks.append({"player_id": player_id, "source": source})

    def mark_entered_play(self, entity_id: str):
        self.entered_play_turn[entity_id] = self.turn_number

    def lock_attack(self, entity_id: str, ability_id: str):
        """Locks an attack through its user's next turn."""
        self.attack_locks[(entity_id, ability_id)] = self.turn_number + 2

    def attack_locked(self, entity_id: str, ability_id: str) -> bool:
        return self.turn_number <= self.attack_locks.get((entity_id, ability_id), 0)

    def lock_retreat(self, entity_id: str, through_turn: Optional[int] = None):
        """Blocks retreat through `through_turn` (default: the opponent's next turn)."""
        self.retreat_locks[entity_id] = (
            self.turn_number + 1 if through_turn is None else through_turn
        )

    def retreat_locked(self, entity_id: str) -> bool:
        return self.turn_number <= self.retreat_locks.get(entity_id, 0)

    def schedule_knockout(self, entity_id: str, at_end_of_turn: int):
        """Marks a Pokemon to be Knocked Out at the end of `at_end_of_turn`."""
        current = self.scheduled_knockouts.get(entity_id)
        if current is None or at_end_of_turn < current:
            self.scheduled_knockouts[entity_id] = at_end_of_turn

    def lock_plays(self, player_id: str, predicate, through_turn: Optional[int] = None):
        """Forbids `player_id` playing hand cards matching `predicate`
        (default: through their next turn)."""
        self.play_locks.setdefault(player_id, []).append(
            (predicate, self.turn_number + 1 if through_turn is None else through_turn)
        )

    def play_locked(self, player_id: str, card: Any) -> bool:
        return any(
            (exp is None or self.turn_number <= exp) and pred(card)
            for pred, exp in self.play_locks.get(player_id, [])
        )

    def restrict_attachments(self, entity_id: str, through_turn: Optional[int] = None):
        """Forbids energy attachments onto `entity_id` (default: through the
        opponent's next turn)."""
        self.attach_restrictions[entity_id] = (
            self.turn_number + 1 if through_turn is None else through_turn
        )

    def attach_restricted(self, entity_id: str) -> bool:
        return self.turn_number <= self.attach_restrictions.get(entity_id, -1)

    def set_attack_flip_check(self, entity_id: str, through_turn: Optional[int] = None,
                              title: str = ""):
        """Requires a coin flip before `entity_id` attacks (tails = the attack
        doesn't happen); default lifetime: through the opponent's next turn."""
        self.attack_flip_checks[entity_id] = (
            self.turn_number + 1 if through_turn is None else through_turn,
            title,
        )

    def attack_flip_check(self, entity_id: str) -> Optional[str]:
        """The flip title when `entity_id` must flip to attack this turn, else None."""
        entry = self.attack_flip_checks.get(entity_id)
        if entry is not None and self.turn_number <= entry[0]:
            return entry[1]
        return None

    def may_evolve_target(self, entity_id: str) -> bool:
        """A Pokemon may evolve only if it has been in play since a previous
        turn, and never during either player's first turn (turns 1 and 2)."""
        if self.turn_number <= 2:
            return False
        if entity_id in self.devolved_this_turn:
            return False
        return self.entered_play_turn.get(entity_id, 0) < self.turn_number


def selectable_action(
    game_id: str,
    action_id: str,
    description: str,
    selection_type: str = SELECTION_TYPE_PLAY,
) -> Dict[str, Any]:
    """Builds a SelectableAction wire dict."""
    return {
        "gameID": game_id,
        "actionID": action_id,
        "description": description,
        "selectionType": selection_type,
    }


def entity_list_target_info(
    valid_targets: List[str],
    number_to_select: int = 1,
    minimum_to_select: int = 1,
    forced: bool = True,
    kind: str = SelectionKind.ENTITY_LIST.value,
) -> Dict[str, Any]:
    """Builds an interactive EntityListTargetInformation wire dict."""
    return {
        "name": kind,
        "selected": True,
        "validTargets": valid_targets,
        "numberToSelect": number_to_select,
        "minimumToSelect": minimum_to_select,
        "forced": forced,
    }


def _target_map_entry(
    game_id: str,
    entity_id: str,
    action_id: str,
    description: str,
    target_infos: Optional[List[Dict[str, Any]]] = None,
    selection_type: str = SELECTION_TYPE_PLAY,
) -> Dict[str, Any]:
    return {
        "entityID": entity_id,
        "selectableAction": selectable_action(
            game_id, action_id, description, selection_type
        ),
        "targetInfoLst": target_infos or [],
    }


def energy_provided_count(energy: EnergyEntity, board: Optional[BoardState] = None) -> int:
    """How much one energy card pays toward a cost (client s.y: max option
    length); with a board, provided-modifying passives apply."""
    options = energy_provided_options(board, energy)
    return max((len(option) for option in options), default=1)


def _energy_provided_types(energy: EnergyEntity, board: Optional[BoardState] = None) -> set:
    """The set of types one energy can provide (union of the options)."""
    provided = set()
    for option in energy_provided_options(board, energy):
        provided.update(option)
    return provided


def attack_cost_satisfied(cost: Dict[str, int], energies: List[EnergyEntity],
                          board: Optional[BoardState] = None) -> bool:
    """Whether the attached energies can pay an attack's cost.

    Each card pays up to its provided count (Double Turbo pays 2); typed
    requirements consume the most type-constrained cards first, colorless
    accepts whatever capacity remains.
    """
    pool = [
        {"types": _energy_provided_types(e, board), "count": energy_provided_count(e, board)}
        for e in energies
    ]
    colorless_needed = 0
    for type_key, count in (cost or {}).items():
        # Wire cost keys are client enum names ("Grass"); accept legacy ints too.
        if type_key in POKEMON_TYPES_BY_CLIENT_NAME:
            type_val = POKEMON_TYPES_BY_CLIENT_NAME[type_key].value
        else:
            type_val = int(type_key)
        if type_val in _WILDCARD_COST_TYPES:
            colorless_needed += count
            continue
        for _ in range(count):
            candidates = [p for p in pool if type_val in p["types"]]
            if not candidates:
                return False
            candidates.sort(key=lambda p: len(p["types"]))
            chosen = candidates[0]
            chosen["count"] -= 1
            if chosen["count"] <= 0:
                pool.remove(chosen)
    return sum(p["count"] for p in pool) >= colorless_needed


def pokemon_without_tool(pokemon: Any) -> bool:
    """A Pokemon may hold one Pokemon Tool (server rule; client has no cap)."""
    return not any(
        child.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value
        for child in pokemon.children
    )


def _active_immobilized(board: BoardState, player_id: str) -> bool:
    """Asleep/Paralyzed Actives can neither attack nor retreat."""
    active = board.active_pokemon(player_id)
    conditions = active.get_attribute(AttrID.SPECIAL_CONDITIONS) if active else None
    return any(c in _IMMOBILIZING_CONDITIONS for c in (conditions or []))


def compute_legal_actions(
    board: BoardState,
    state: TurnState,
    player_id: str,
    game_id: str,
) -> List[Dict[str, Any]]:
    """All legal plays for the acting player, as targetMap entries."""
    entries: List[Dict[str, Any]] = []

    hand_area = board.find_player_area(player_id, "hand")
    bench_area = board.find_player_area(player_id, "bench")
    if not hand_area or not bench_area:
        return entries

    in_play = board.pokemon_in_play(player_id)
    in_play_ids = [p.entity_id for p in in_play]
    deck_area = board.find_player_area(player_id, "deck")
    deck_cards = deck_area.children if deck_area else []
    bench_has_space = len(bench_area.children) < effective_bench_capacity(board, player_id)

    for card in hand_area.children:
        if isinstance(card, PokemonEntity):
            # A play lock can name Pokemon as well as Trainers ("can't play
            # any cards from your hand", "can't put Pokemon with an Ability
            # into play"), so it is asked of every card in hand and not only
            # of the fossils. Every Item/Supporter/Energy lock in the pool
            # takes a predicate that says no to a Pokemon, so nothing else
            # changes.
            if state.play_locked(player_id, card):
                continue
            stage = card.get_attribute(AttrID.STAGE)
            if unplayable_from_hand_now(board, player_id, card):
                continue  # Shedinja / Palafin ex: enters play only via an effect
            if stage == PokemonStage.BASIC.value:
                # Fossils stay Item cards in hand: Item locks gate the bench play.
                if (card.get_attribute(AttrID.TRAINER_TYPE) is not None
                        and trainer_play_blocked(board, player_id, card)):
                    continue
                # Eternal Zone: no non-Darkness Pokemon (fossils included)
                # may be put into play.
                if putting_into_play_blocked(board, player_id, card):
                    continue
                if bench_has_space:
                    # The bench area is the drop target; without it the drag
                    # dead-ends at the ActionsNode and nothing highlights.
                    entries.append(_target_map_entry(
                        game_id, card.entity_id,
                        action_id_for(card.entity_id, "play"), ACTION_PLAY_POKEMON,
                        [entity_list_target_info([bench_area.entity_id])],
                    ))
                continue

            # Swelling Flash (Luxray PAL): a hand Ability that puts this
            # evolved Pokemon onto the Bench. Same drop target as a Basic.
            bench_from_hand = getattr(def_for(card.archetype_id), "bench_from_hand", None)
            if (bench_from_hand is not None and bench_has_space
                    and not abilities_disabled(board, card)
                    and not putting_into_play_blocked(board, player_id, card)
                    and bench_from_hand(board, player_id, card)):
                entries.append(_target_map_entry(
                    game_id, card.entity_id,
                    action_id_for(card.entity_id, "play"), ACTION_PLAY_POKEMON,
                    [entity_list_target_info([bench_area.entity_id])],
                ))
            evolves_from = card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)
            if not evolves_from:
                continue
            # Eternal Zone: evolving puts the evolution card into play, so a
            # non-Darkness evolution is refused (devolving is not: the
            # pre-evolution was already in play).
            if putting_into_play_blocked(board, player_id, card):
                continue
            evolve_targets = [
                p.entity_id for p in in_play
                if (p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == evolves_from
                    or can_evolve_onto(board, p, card))
                and not evolution_blocked(board, player_id, p)
                and (state.may_evolve_target(p.entity_id)
                     or can_evolve_early(board, p)
                     or (state.turn_number > 2
                         and can_evolve_same_turn(board, p, card)))
            ]
            if evolve_targets:
                entries.append(_target_map_entry(
                    game_id, card.entity_id,
                    action_id_for(card.entity_id, "evolve"), ACTION_EVOLVE,
                    [entity_list_target_info(evolve_targets)],
                ))

        elif isinstance(card, EnergyEntity):
            if state.energy_attached or not in_play_ids:
                continue
            if state.play_locked(player_id, card):
                continue
            definition = def_for(card.archetype_id)
            condition = getattr(definition, "attach_condition", None)
            if condition is not None and not condition(board, player_id):
                continue
            attach_to = getattr(definition, "attach_to", None)
            targets = [
                p.entity_id for p in in_play
                if (attach_to is None or attach_to(p))
                and not state.attach_restricted(p.entity_id)
            ]
            if targets:
                entries.append(_target_map_entry(
                    game_id, card.entity_id,
                    action_id_for(card.entity_id, "energy"), ACTION_PLAY_ENERGY,
                    [entity_list_target_info(targets)],
                ))

        elif isinstance(card, TrainerEntity):
            trainer_type = card.get_attribute(AttrID.TRAINER_TYPE)
            if state.play_locked(player_id, card) \
                    or trainer_play_blocked(board, player_id, card):
                continue
            definition = def_for(card.archetype_id)
            condition = getattr(definition, "condition", None)
            if condition is not None \
                    and not trainer_condition_met(condition, board, player_id, card):
                continue
            # "Search your deck for..." with an empty deck is nothing to
            # do, so the card is not offered at all. Nothing in the pool
            # puts cards INTO the deck before searching it, so the count
            # here is the count the search itself would see.
            if searches_deck(definition) and not deck_cards:
                continue
            if trainer_type == TrainerType.ITEM.value:
                entries.append(_target_map_entry(
                    game_id, card.entity_id,
                    action_id_for(card.entity_id, "item"), ACTION_USE_TRAINER,
                ))
            elif trainer_type == TrainerType.SUPPORTER.value:
                # Normally Supporters are illegal on turn 1 (going first).
                # Cards like Team Rocket's Proton set usable_first_turn.
                first_ok = bool(getattr(definition, "usable_first_turn", False))
                if state.supporter_plays < supporter_play_limit(board, player_id) and (
                    state.turn_number > 1 or first_ok
                ):
                    entries.append(_target_map_entry(
                        game_id, card.entity_id,
                        action_id_for(card.entity_id, "supporter"), ACTION_USE_TRAINER,
                    ))
            elif trainer_type == TrainerType.STADIUM.value:
                if not state.stadium_played and not _same_stadium_in_play(board, card):
                    entries.append(_target_map_entry(
                        game_id, card.entity_id,
                        action_id_for(card.entity_id, "stadium"), ACTION_PLAY_STADIUM,
                    ))
            elif trainer_type == TrainerType.POKEMON_TOOL.value:
                if tool_attach_blocked(board, player_id):
                    continue
                tool_attach_to = getattr(definition, "attach_to", None)
                tool_targets = [
                    p.entity_id for p in in_play
                    if tool_slots_free(board, p) > 0
                    and (tool_attach_to is None or tool_attach_to(p))
                ]
                if tool_targets:
                    entries.append(_target_map_entry(
                        game_id, card.entity_id,
                        action_id_for(card.entity_id, "tool"), ACTION_ATTACH_TOOL,
                        [entity_list_target_info(tool_targets)],
                    ))

    entries.extend(_ability_entries(board, state, player_id, game_id, in_play))
    entries.extend(_out_of_zone_ability_entries(board, state, player_id, game_id))
    entries.extend(_stadium_ability_entries(board, state, player_id, game_id))
    # Asleep/Paralyzed gates attacks per-attack (Attack(usable_despite_conditions)).
    immobilized = _active_immobilized(board, player_id)
    entries.extend(_attack_entries(board, state, player_id, game_id, immobilized))
    # Retreat has its own exemption (Escape Board), asked of the Active only.
    active = board.active_pokemon(player_id)
    if not immobilized or (active is not None
                           and can_retreat_despite_conditions(board, active)):
        entries.extend(_retreat_entry(board, state, player_id, game_id))
    # A turn kept alive past an attack (Fluffy Barrage / Festival Lead) stays
    # in the attack phase: only attacking (or End Turn) remains legal. The
    # session asks "perform another attack?" before re-offering.
    if state.attacks_used:
        entries = [
            e for e in entries
            if e["selectableAction"]["description"] == ACTION_USE_ATTACK
        ]
    return entries


def _ability_entries(
    board: BoardState,
    state: TurnState,
    player_id: str,
    game_id: str,
    in_play: List[PokemonEntity],
) -> List[Dict[str, Any]]:
    """Usable activated abilities on the player's in-play Pokemon."""
    entries = []
    for pokemon in in_play:
        locked = ability_locked(board, pokemon)
        for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
            if not isinstance(entry, dict):
                continue
            ability_id = entry.get("abilityID")
            ability = ABILITIES_BY_ID.get(ability_id) if ability_id else None
            if ability is None or ability.activation not in (
                    Activations.ONCE_PER_TURN, Activations.UNLIMITED):
                continue
            # Hand/discard-only abilities (Pyukumuku, Beedrill, Gengar) are
            # offered from those zones, never from in-play.
            if ability.usable_from:
                continue
            # Path to the Peak locks a Pokemon's own Abilities, but a Tool-
            # granted ability (Forest Seal Stone) lives on the tool, not the
            # Pokemon, so it stays usable; a card's own rules text (a
            # fossil's discard, Lillie's Poke Doll's return) is no Ability
            # at all, so no lock reaches it.
            if locked and not ability.is_granted and not ability.rules_text:
                continue
            if ability.activation != Activations.UNLIMITED \
                    and (pokemon.entity_id, ability_id) in state.used_abilities:
                continue
            if ability.vstar and player_id in state.vstar_used:
                continue
            if ability.effect is None:
                continue
            if ability.shared_once_per_turn \
                    and ability.shared_once_per_turn in state.used_named_abilities:
                continue
            if ability.condition and not ability.condition(board, player_id, pokemon):
                continue
            # The actionID must be the PIE_ABILITIES abilityID so the pulled-
            # back panel can resolve the ability's text.
            entries.append(_target_map_entry(
                game_id, pokemon.entity_id, ability_id, ACTION_USE_ABILITY,
                selection_type=SELECTION_TYPE_PANEL,
            ))
    return entries


def _out_of_zone_ability_entries(
    board: BoardState, state: TurnState, player_id: str, game_id: str
) -> List[Dict[str, Any]]:
    """Abilities flagged usable_from='hand'/'discard' on the player's cards in
    those zones, each offered with its own client selection flow.

    Hand sources get AbilitySelection (click -> ability panel) plus OutOfPlay
    (playmat drag). Discard sources get the panel alone: OutOfPlay disables
    clicks there, which soft-locked the ability.

    Ruling: the usual ability locks (Path to the Peak) read "Pokemon in play",
    so they do NOT gate hand/discard sources. A lock that names these zones
    (Garbotoxin) answers blocks_out_of_play_abilities instead, and that one
    does gate them.
    """
    entries = []
    for zone in ("hand", "discard"):
        area = board.find_player_area(player_id, zone)
        for card in (area.children if area else []):
            locked = out_of_play_ability_locked(board, card)
            for entry in card.get_attribute(AttrID.PIE_ABILITIES) or []:
                if not isinstance(entry, dict):
                    continue
                ability_id = entry.get("abilityID")
                ability = ABILITIES_BY_ID.get(ability_id) if ability_id else None
                if ability is None or ability.usable_from != zone:
                    continue
                if ability.effect is None:
                    continue
                # A Trainer's own rules text (Grant) is no Ability: no lock.
                if locked and not ability.rules_text:
                    continue
                if ability.activation not in (
                        Activations.ONCE_PER_TURN, Activations.UNLIMITED):
                    continue
                if ability.activation != Activations.UNLIMITED \
                        and (card.entity_id, ability_id) in state.used_abilities:
                    continue
                if ability.vstar and player_id in state.vstar_used:
                    continue
                if ability.shared_once_per_turn \
                        and ability.shared_once_per_turn in state.used_named_abilities:
                    continue
                if ability.condition and not ability.condition(board, player_id, card):
                    continue
                # Hand: AbilitySelection opens the ability panel so Pitch can
                # coexist with a Basic's drag-to-bench play, and the second
                # entry below keeps the playmat-drop path.
                if zone == "hand":
                    entries.append(_target_map_entry(
                        game_id, card.entity_id, ability_id, ACTION_USE_ABILITY,
                        selection_type=SELECTION_TYPE_PANEL,
                    ))
                entries.append(_target_map_entry(
                    game_id, card.entity_id, ability_id, ACTION_USE_ABILITY,
                    # OutOfPlay disables clicks; discard cards need the ability panel.
                    selection_type=(SELECTION_TYPE_PANEL if zone == "discard"
                                    else SelectionKind.OUT_OF_PLAY.value),
                ))
    return entries


def _stadium_ability_entries(
    board: BoardState, state: TurnState, player_id: str, game_id: str
) -> List[Dict[str, Any]]:
    """The in-play Stadium's activated ability (Training Court), offered once
    during each player's turn. Only the active player is offered actions and
    used_abilities resets each turn, so (stadium, ability) is a clean
    once-per-player-turn key."""
    stadium_area = board.find_global_area("activeStadium")
    entries = []
    for stadium in (stadium_area.children if stadium_area else []):
        definition = def_for(stadium.archetype_id)
        ability = getattr(definition, "ability", None)
        if ability is None or ability.effect is None or not ability.ability_id:
            continue
        if (stadium.entity_id, ability.ability_id) in state.used_abilities:
            continue
        if ability.condition and not ability.condition(board, player_id, stadium):
            continue
        entries.append(_target_map_entry(
            game_id, stadium.entity_id, ability.ability_id, ACTION_USE_ABILITY,
            selection_type=SELECTION_TYPE_PANEL,
        ))
    return entries


def _retreat_entry(
    board: BoardState, state: TurnState, player_id: str, game_id: str
) -> List[Dict[str, Any]]:
    """Retreat offer for the Active (once per turn, cost payable, bench occupied)."""
    if state.retreated:
        return []
    active = board.active_pokemon(player_id)
    if not active:
        return []
    if state.retreat_locked(active.entity_id) or retreat_blocked(board, active):
        return []
    bench_area = board.find_player_area(player_id, "bench")
    bench_ids = [
        c.entity_id for c in (bench_area.children if bench_area else [])
        if isinstance(c, PokemonEntity)
    ]
    if not bench_ids:
        return []
    cost = effective_retreat_cost(board, active)
    energies = board.attached_energies(active)
    if sum(energy_provided_count(e, board) for e in energies) < cost:
        return []

    # New active FIRST, cost LAST: the Done button only renders on a node with
    # no successor (NodeToAdvanceTo()==null), and SelectingForAnAbility()
    # special-cases the RetreatNewActive kind as an action's first node.
    new_active_info = entity_list_target_info(
        bench_ids, kind=SelectionKind.RETREAT_NEW_ACTIVE.value
    )
    new_active_info["targetPrompt"] = {"id": PROMPT_RETREAT_NEW_ACTIVE}
    infos = [new_active_info]
    if cost > 0:
        # d.j's pip tray tallies each picked card's provided amount against
        # valueToSelect (a double energy pays 2); numberToSelect only caps
        # the card count. targetPrompt is the tray's label (it caches the
        # last prompt shown, so leaving it unset displays stale text).
        info = entity_list_target_info(
            [e.entity_id for e in energies],
            number_to_select=cost,
            minimum_to_select=-1,
            kind=SelectionKind.RETREAT_COST_ENTITY_LIST.value,
        )
        info["valueToSelect"] = cost
        info["targetPrompt"] = {"id": PROMPT_RETREAT_COST}
        infos.append(info)
    return [_target_map_entry(
        game_id, active.entity_id,
        action_id_for(active.entity_id, "retreat"), ACTION_RETREAT,
        infos, selection_type=SELECTION_TYPE_PANEL,
    )]


def trainer_condition_met(condition, board: BoardState, player_id: str, card) -> bool:
    """condition(board, player_id[, card]) -- 3-arg variants get the specific
    hand copy (Nugget's turn-draw provenance is per-card)."""
    code = getattr(condition, "__code__", None)
    if code is not None and code.co_argcount >= 3:
        return bool(condition(board, player_id, card))
    return bool(condition(board, player_id))


def _same_stadium_in_play(board: BoardState, card: TrainerEntity) -> bool:
    """A Stadium is unplayable if one with the same archetype is in play."""
    stadium_area = board.find_global_area("activeStadium")
    return any(
        getattr(existing, "archetype_id", None) == card.archetype_id
        for existing in (stadium_area.children if stadium_area else [])
    )


# The floating attack panel is a fixed list, not a scroll list: past this
# many rows it runs off the screen. Borrowed attacks (Mew ex's Memory
# Spiral, Ditto's Sudden Transformation) that would push a Pokemon past it
# collapse into one "Borrowed Attacks" row that opens the scrollable
# attack-choice list (the Genome Hacking picker) instead.
PANEL_ROW_LIMIT = 5
BORROWED_ATTACKS_VERB = "borrowed-attacks"
BORROWED_ATTACKS_TITLE = "Borrowed Attacks"


def borrowed_attacks_action_id(pokemon_entity_id: str) -> str:
    """The synthetic attack row's abilityID for `pokemon`."""
    return action_id_for(pokemon_entity_id, BORROWED_ATTACKS_VERB)


def borrowed_attacks_row(pokemon_entity_id: str, count: int) -> Dict[str, Any]:
    """The PIE_ABILITIES row standing in for `count` borrowed attacks."""
    return {
        "abilityType": "Attack",
        "title": {"id": BORROWED_ATTACKS_TITLE},
        "gameText": {"id": f"Choose 1 of the {count} attacks this Pok\u00e9mon can "
                           "use from other cards."},
        "abilityID": borrowed_attacks_action_id(pokemon_entity_id),
        "cost": {},
        "damage": 0,
        "amountOperator": "",
    }


def attack_usable(
    board: BoardState, state: TurnState, player_id: str, active: PokemonEntity,
    ability_id: str, cost_dict: Dict[str, int], energies, immobilized: bool,
    first_turn_ok: bool,
) -> bool:
    """Every gate one attack row of the Active passes before it is offered:
    locks, Festival Lead's printed-only repeat, Special Conditions, the
    turn-1 ban, VSTAR/GX usage, the attack's own condition, and the Energy
    cost after cost-modifying passives."""
    if state.attack_locked(active.entity_id, ability_id):
        return False
    definition = ABILITIES_BY_ID.get(ability_id)
    # Festival Lead's extra attack repeats an attack this Pokemon HAS, so
    # one lent by a Tool or an Energy is not on offer for it.
    if state.attacks_used and state.extra_attack_printed_only \
            and getattr(definition, "is_granted", False):
        return False
    # Asleep/Paralyzed suppression, per-attack exemptable (Windup Arm).
    if immobilized and not getattr(definition, "usable_despite_conditions", False):
        return False
    # The player going first cannot attack on turn 1 unless the attack
    # explicitly allows it (Indeedee's Watch Over).
    if not (first_turn_ok or getattr(definition, "usable_first_turn", False)):
        return False
    if definition is not None and definition.vstar \
            and player_id in state.vstar_used:
        return False
    if definition is not None and definition.gx \
            and not state.gx_available(player_id, active, board):
        return False
    # Attack usage restriction ("You can use this attack only if...").
    if definition is not None and definition.condition is not None \
            and not definition.condition(board, player_id, active):
        return False
    # Cost-modifying passives (e.g. Excited Heart) apply here.
    cost = effective_attack_cost(board, active, cost_dict or {})
    return attack_cost_satisfied(cost, energies, board)


def usable_borrowed_attacks(
    board: BoardState, state: TurnState, player_id: str, active: PokemonEntity,
    immobilized: bool = False,
) -> List[Tuple[Any, Any]]:
    """The (owner, attack) pairs behind the Borrowed Attacks row that the
    Active could declare right now."""
    if attacking_blocked(board, active):
        return []
    if immobilized and can_attack_despite_conditions(board, active):
        immobilized = False
    first_turn_ok = state.turn_number > 1 or can_attack_first_turn(board, active)
    energies = board.attached_energies(active)
    return [
        (owner, attack)
        for owner, attack in granted_extra_attacks_with_owner(board, active)
        if attack.ability_id and attack_usable(
            board, state, player_id, active, attack.ability_id,
            attack.to_dict().get("cost") or {}, energies, immobilized,
            first_turn_ok)
    ]


def _attack_entries(
    board: BoardState, state: TurnState, player_id: str, game_id: str,
    immobilized: bool = False,
) -> List[Dict[str, Any]]:
    """Usable attacks of the Active Pokemon (energy requirement met)."""
    active = board.active_pokemon(player_id)
    if not active:
        return []
    # A passive can stop this Pokemon attacking at all (Disgusting Pollen).
    if attacking_blocked(board, active):
        return []
    # A passive (Windup Arm) can exempt the whole Pokemon from the gate.
    if immobilized and can_attack_despite_conditions(board, active):
        immobilized = False
    # Meloetta ex's Debut Performance lifts the turn-1 ban for every attack
    # this Pokemon has, where usable_first_turn lifts it one attack at a time.
    first_turn_ok = state.turn_number > 1 or can_attack_first_turn(board, active)
    abilities = active.get_attribute(AttrID.PIE_ABILITIES) or []
    if not isinstance(abilities, list):
        logging.warning(
            f"[LegalActions] Unparsed PIE_ABILITIES on {active.entity_id}: {abilities!r}"
        )
        return []

    energies = board.attached_energies(active)
    grouped_id = borrowed_attacks_action_id(active.entity_id)
    entries = []
    for ability in abilities:
        # abilityType carries the PieAbilityDescription class-name hint string.
        if ability.get("abilityType") != "Attack":
            continue
        ability_id = ability.get("abilityID")
        if not ability_id:
            continue  # legacy scripts without ability IDs can't be offered
        if ability_id == grouped_id:
            # The stand-in row: on offer while any attack behind it is.
            usable = bool(usable_borrowed_attacks(
                board, state, player_id, active, immobilized))
        else:
            usable = attack_usable(
                board, state, player_id, active, ability_id,
                ability.get("cost") or {}, energies, immobilized, first_turn_ok)
        if usable:
            entries.append(_target_map_entry(
                game_id, active.entity_id, ability_id, ACTION_USE_ATTACK,
                selection_type=SELECTION_TYPE_PANEL,
            ))
    return entries


# TargetInformation kind: l.m node -> command l.L renders the choices (full
# PieAbilityDescription rows: cost pips, damage, owner type) in the panel's
# bonus ability scroll list.
KIND_CAKE_ATTACK_CHOICE = "CakeAttackCustomChoiceTargetInformation"


def copy_attack_choice_node(
    source_entity_id: str,
    candidates: List[Tuple[Any, Any]],
    prompt: str = "",
) -> Dict[str, Any]:
    """A CakeAttackCustomChoiceTargetInformation node whose `choices` are the
    [(pokemon, attack)] candidates' PieAbilityDescription dicts; the reply
    rides an IntTargetResponse (`amount` = candidate index). Never build one
    from an empty list (l.L's scroll list would soft-lock)."""
    choices: List[Dict[str, Any]] = []
    for i, (pokemon, attack) in enumerate(candidates):
        row = attack.to_dict()
        # Each choice needs its own GUID: l.L matches the clicked button by ID.
        row["abilityID"] = action_id_for(source_entity_id, f"copychoice:{i}")
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        row["bonusInfo"] = {
            "originalOwnerTypes": list(types) or [PokemonTypes.COLORLESS.value]
        }
        choices.append(row)
    return {
        "name": KIND_CAKE_ATTACK_CHOICE,
        "selected": True,
        "targetPrompt": {"id": prompt},
        "sortType": None,
        "choices": choices,
    }
