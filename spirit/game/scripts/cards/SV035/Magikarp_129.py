"""Magikarp (SV035 129 -- JP SV2a 129; English MEW/129). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def splashy_splash(ctx):
    heads = await ctx.flip_until_tails("Splashy Splash")
    if heads:
        await ctx.draw_cards(heads)


card = PokemonCardDef(
    guid="51e9adfd-4515-5f8b-b4a3-ecf169e6c04a",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic"],
    subtypes=["Basic"],
    collector_number=129,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Splashy Splash",
            game_text="Flip a coin until you get tails. For each heads, draw a card.",
            cost={PokemonTypes.WATER: 1},
            effect=splashy_splash,
        ),
    ],
)
