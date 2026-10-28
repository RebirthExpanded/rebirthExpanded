"""Shinx (SV2 68 -- JP SVC 005; English PAL/68). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


def _big_roar_condition(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    bench = board.find_player_area(other, "bench") if other else None
    return board.active_pokemon(player_id) is pokemon and bool(bench and bench.children)


async def big_roar(ctx):
    await su.opponent_switches(ctx)


card = PokemonCardDef(
    guid="364b0903-f0f6-55ae-8125-6926e30535ae",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    display_name="Shinx",
    searchable_by=["Shinx", "Basic"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=403,
    abilities=[
        Ability(
            title="Big Roar",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            activation=Activations.ONCE_PER_TURN,
            condition=_big_roar_condition,
            effect=big_roar,
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
