"""Mabosstiff (SV045 63 -- JP SV1V 055; English PAF/188, PAF/63, SVI/137, SVI/218). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


def _howl_condition(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    bench = board.find_player_area(other, "bench") if other else None
    return bool(bench and bench.children)


async def intimidating_howl(ctx):
    await su.opponent_switches(ctx)


card = PokemonCardDef(
    guid="5acd2abd-8293-59cc-8e56-2870d9a8b1a2",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mabosstiff.Name",
    display_name="Mabosstiff",
    searchable_by=["Mabosstiff", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    family_id=942,
    abilities=[
        Ability(
            title="Intimidating Howl",
            game_text="Once during your turn, you may switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            activation=Activations.ONCE_PER_TURN,
            condition=_howl_condition,
            effect=intimidating_howl,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=ac.recoil_attack(30),
        ),
    ],
)
