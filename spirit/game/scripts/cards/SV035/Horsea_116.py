"""Horsea (SV035 116 -- JP SV2a 116; English MEW/116). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="7f715e41-1ee4-53af-bf92-c7db9d6c88f5",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    display_name="Horsea",
    searchable_by=["Horsea", "Basic"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Rain Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Sharp Fin",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
