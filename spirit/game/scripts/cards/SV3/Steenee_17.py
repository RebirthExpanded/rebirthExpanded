"""Steenee (SV3 17 -- JP SV2P 008; English OBF/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def aromatherapy(ctx):
    for p in ctx.my_pokemon_in_play():
        await ctx.heal(30, p)


card = PokemonCardDef(
    guid="4c8c1d9a-f852-5a6b-af7b-7709bc6dc5eb",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    display_name="Steenee",
    searchable_by=["Steenee", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name",
    family_id=761,
    abilities=[
        Attack(
            title="Aromatherapy",
            game_text="Heal 30 damage from each of your Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=aromatherapy,
        ),
        Attack(
            title="Razor Leaf",
            game_text="",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
        ),
    ],
)
