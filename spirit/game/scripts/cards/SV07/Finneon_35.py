"""Finneon (SV07 35 -- JP SV7 020; English SCR/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="81a54261-badd-541c-829a-85b332802015",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name",
    display_name="Finneon",
    searchable_by=["Finneon", "Basic"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=456,
    abilities=[
        Attack(
            title="Sprinkle Water",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
