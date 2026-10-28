"""Tentacool (SV035 72 -- JP SV2a 072; English MEW/72). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="293808ec-d3cd-57a1-a153-2c7b3d44808c",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    display_name="Tentacool",
    searchable_by=["Tentacool", "Basic"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=72,
    abilities=[
        Attack(
            title="Tingle",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Watering",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
