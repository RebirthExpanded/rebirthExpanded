"""Arceus & Dialga & Palkia-GX (SM - Cosmic Eclipse 156/236 --
JP SM12 065/095).

Basic Dragon TAG TEAM Pokemon-GX. HP 280, weakness Fairy x2, no
resistance, retreat 3.

  Ultimate Ray        [WMC] 150  Search your deck for up to 3 basic Energy
                                 cards and attach them to your Pokemon in
                                 any way you like. Then, shuffle your deck.
  Altered Creation-GX [M]        For the rest of this game, your Pokemon's
                                 attacks do 30 more damage to your
                                 opponent's Active Pokemon (before applying
                                 Weakness and Resistance). With 1 extra [W]
                                 Energy attached, take 1 more Prize card
                                 when one of your Pokemon's attacks Knocks
                                 Out your opponent's Active Pokemon.

Both halves last the whole game, which the engine now supports directly:
the +30 is a TurnDamageModifier marked permanent (so the turn rollover
stops pruning it) and the Prize clause is an extra-prize watcher marked
the same way. Neither is tied to this Pokemon -- they stay after it is
Knocked Out, which is what "for the rest of this game" means.

The +30 lands before Weakness, which falls out of where the turn
modifiers are applied in compute_damage: after the attacker-side passives
and before Weakness and Resistance.

The Prize clause reads the opponent's ACTIVE at knockout time, and the
watcher is consulted pre-move so the Active spot still holds the Pokemon
that was knocked out.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_basic_energy
from spirit.game.session.legal_actions import attack_cost_satisfied
from spirit.game.session.passives import TurnDamageModifier

BOOST = 30
# The [M] cost plus the one extra [W], asked as a single question.
_COST_PLUS_EXTRA = {"Metal": 1, "Water": 1}


async def altered_creation_gx(ctx):
    """+30 for the rest of the game, and with an extra [W], a Prize with it."""
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        BOOST, ctx.player_id, opposing_active_only=True, permanent=True))
    energies = ctx.attached_energies(ctx.attacker)
    if not attack_cost_satisfied(_COST_PLUS_EXTRA, energies, ctx.board):
        return
    board = ctx.board
    opponent_id = ctx.opponent_id

    def _their_active(pokemon):
        return board.active_pokemon(opponent_id) is pokemon

    ctx.add_extra_prize_watcher(target_predicate=_their_active, prizes=1,
                                permanent=True)


card = PokemonCardDef(
    guid="b9221a4f-c209-584a-85d5-f146041ef662",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusDialgaPalkiaGX.Name",
    display_name="Arceus & Dialga & Palkia-GX",
    searchable_by=["Arceus & Dialga & Palkia-GX", "Basic", "TAG TEAM", "GX",
                   "ArceusDialgaPalkiaGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=156,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=493,
    abilities=[
        Attack(
            title="Ultimate Ray",
            game_text="Search your deck for up to 3 basic Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1,
                  PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=search_attach_energy(predicate=is_basic_energy, count=3,
                                        distribute=True),
        ),
        Attack(
            title="Altered Creation-GX",
            game_text="For the rest of this game, your Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). If this Pokémon has at least 1 extra Water Energy attached to it (in addition to this attack's cost), take 1 more Prize card when one of your Pokémon's attacks Knocks Out your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1},
            gx=True,
            effect=altered_creation_gx,
        ),
    ],
)
