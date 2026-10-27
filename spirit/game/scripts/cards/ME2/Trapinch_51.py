"""Trapinch (ME2 51 -- JP M2 045; English PFL/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="929b36d2-515d-593d-8075-9bc2d9e46cbf",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    display_name="Trapinch",
    searchable_by=["Trapinch", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=328,
    abilities=[
        Attack(
            title="Double Headbutt",
            game_text="Flip 2 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=10),
        ),
    ],
)
