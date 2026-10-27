"""Zangoose (SV08 149 -- JP SV8 085; English SSP/149). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def fury_cutter(ctx):
    heads = sum(1 for r in await ctx.flip_coins(3, "Fury Cutter") if r)
    await ctx.deal_damage(10 + {0: 0, 1: 20, 2: 50, 3: 80}[heads])


card = PokemonCardDef(
    guid="e290edee-7b3c-504e-be74-c693d4291a8c",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name",
    display_name="Zangoose",
    searchable_by=["Zangoose", "Basic"],
    subtypes=["Basic"],
    collector_number=149,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Fury Cutter",
            game_text="Flip 3 coins. If 1 of them is heads, this attack does 20 more damage. If 2 of them are heads, this attack does 50 more damage. If all of them are heads, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=fury_cutter,
        ),
    ],
)
