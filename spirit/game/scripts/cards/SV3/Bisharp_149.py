"""Bisharp (SV3 149 -- JP SV3 081; English OBF/149). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def fury_cutter(ctx):
    heads = sum(1 for r in await ctx.flip_coins(3, "Fury Cutter") if r)
    await ctx.deal_damage(50 + {0: 0, 1: 20, 2: 60, 3: 120}[heads])


card = PokemonCardDef(
    guid="633e9456-79d2-5395-986c-dca234f1d932",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    display_name="Bisharp",
    searchable_by=["Bisharp", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=149,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    family_id=624,
    abilities=[
        Attack(
            title="Metal Claw",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
        Attack(
            title="Fury Cutter",
            game_text="Flip 3 coins. If 1 of them is heads, this attack does 20 more damage. If 2 of them are heads, this attack does 60 more damage. If all of them are heads, this attack does 120 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=fury_cutter,
        ),
    ],
)
