"""Bulbasaur (BWPJ 124 -- JP BWP 124; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="bf0bd889-9be8-53d2-b373-f27a666c8fed",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    display_name="Bulbasaur",
    searchable_by=["Bulbasaur", "Basic"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=1,
    abilities=[
        Attack(
            title="Sleep Powder",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
