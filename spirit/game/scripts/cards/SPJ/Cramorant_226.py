"""Cramorant (SPJ 226 -- JP SP 226; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="924ef10e-9ddd-5675-bb9e-9fdd29288d83",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cramorant.Name",
    display_name="Cramorant",
    searchable_by=["Cramorant", "Basic"],
    subtypes=["Basic"],
    collector_number=226,
    set_code="SPJ",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=845,
    abilities=[
        Attack(
            title="Triple Stab",
            game_text="Flip 3 coins. This attack does 60 damage for each heads.",
            cost={PokemonTypes.WATER: 3},
            damage=60,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=60),
        ),
    ],
)
