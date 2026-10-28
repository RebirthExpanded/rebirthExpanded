"""Litleo (SV2 31 -- JP SV1a 014; English PAL/31). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def blazing_destruction(ctx):
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="59276c52-5117-547b-b83d-d73a740d9c0d",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    display_name="Litleo",
    searchable_by=["Litleo", "Basic"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=667,
    abilities=[
        Attack(
            title="Blazing Destruction",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=blazing_destruction,
        ),
        Attack(
            title="Live Coal",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
    ],
)
