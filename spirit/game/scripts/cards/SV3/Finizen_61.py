"""Finizen (SV3 61 -- JP SV3 030; English OBF/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="92ed9320-a48c-50f2-b2ab-6fa666dd7846",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    display_name="Finizen",
    searchable_by=["Finizen", "Basic"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=963,
    abilities=[
        Attack(
            title="Tail Smack",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)
