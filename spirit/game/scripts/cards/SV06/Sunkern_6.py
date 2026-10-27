"""Sunkern (SV06 6 -- JP SV6 001; English TWM/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="adccc452-2250-5ffe-b32f-bf59cb439056",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    display_name="Sunkern",
    searchable_by=["Sunkern", "Basic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=191,
    abilities=[
        Attack(
            title="Bullet Seed",
            game_text="Flip 4 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=4, per_heads=10),
        ),
    ],
)
