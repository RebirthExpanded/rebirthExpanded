"""Shellos (SV08 46 -- JP SV8 030; English SSP/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="9976c59f-c7f3-5773-b681-f96167d0c1da",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name",
    display_name="Shellos",
    searchable_by=["Shellos", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=422,
    abilities=[
        Attack(
            title="Sprinkle Water",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
