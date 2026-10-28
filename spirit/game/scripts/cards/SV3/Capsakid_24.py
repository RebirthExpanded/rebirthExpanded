"""Capsakid (SV3 24 -- JP SV3 010; English OBF/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="fe15a2c8-0db5-52fd-88d3-bccb30c1c1c7",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    display_name="Capsakid",
    searchable_by=["Capsakid", "Basic"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=951,
    abilities=[
        Attack(
            title="Double Headbutt",
            game_text="Flip 2 coins. This attack does 50 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=50),
        ),
    ],
)
