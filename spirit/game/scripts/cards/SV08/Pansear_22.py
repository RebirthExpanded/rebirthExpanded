"""Pansear (SV08 22 -- JP SV7a 007; English SSP/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="02876721-7906-5eb5-9a3a-4a44d3eea2c7",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    display_name="Pansear",
    searchable_by=["Pansear", "Basic"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=513,
    abilities=[
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
