"""Heracross (SV2 6 -- JP SV2D 006; English PAL/194, PAL/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def smashing_horn(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="a5504100-24fe-5275-aecf-6bee33eeb9e7",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
        ),
        Attack(
            title="Smashing Horn",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.GRASS: 3},
            damage=110,
            effect=smashing_horn,
        ),
    ],
)
