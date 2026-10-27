"""Rufflet (SV08 152 -- JP SV7a 049; English SSP/152). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="20c2732c-19c3-5fcc-be56-650d36ba4bbd",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    display_name="Rufflet",
    searchable_by=["Rufflet", "Basic"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=627,
    abilities=[
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
