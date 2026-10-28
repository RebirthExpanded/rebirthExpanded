"""Numel (SV3 31 -- JP SV2D 010; English OBF/31). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="177fcce9-4cda-5a8d-a4c5-f1b8821ed2c1",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    display_name="Numel",
    searchable_by=["Numel", "Basic"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=322,
    abilities=[
        Attack(
            title="Hot Magma",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
    ],
)
