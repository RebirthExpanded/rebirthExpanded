"""Toedscool (SV045 4 -- JP SV1V 009; English PAF/105, PAF/4, SVI/201, SVI/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="56ac4663-e8f8-5361-b7f5-8edb99330fa3",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    display_name="Toedscool",
    searchable_by=["Toedscool", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=948,
    abilities=[
        Attack(
            title="Furious Kicks",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=10),
        ),
    ],
)
