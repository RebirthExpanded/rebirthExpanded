"""Fuecoco (SV2 35 -- JP SV1a 018; English PAL/201, PAL/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def spacing_out(ctx):
    results = await ctx.flip_coins(1, "Spacing Out")
    if results and results[0]:
        await ctx.heal(30, ctx.attacker)


card = PokemonCardDef(
    guid="e51b9af4-ccc0-5954-8e82-a39269ee1e79",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name",
    display_name="Fuecoco",
    searchable_by=["Fuecoco", "Basic"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=909,
    abilities=[
        Attack(
            title="Spacing Out",
            game_text="Flip a coin. If heads, heal 30 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=spacing_out,
        ),
        Attack(
            title="Flare",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
