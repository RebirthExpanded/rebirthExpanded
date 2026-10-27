"""Shroodle (SV08 120 -- JP SV8 073; English SSP/120). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="604defb2-6a30-5a86-95f9-fc6cb5486ede",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    display_name="Shroodle",
    searchable_by=["Shroodle", "Basic"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=944,
    abilities=[
        Attack(
            title="Spray Fluid",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)
