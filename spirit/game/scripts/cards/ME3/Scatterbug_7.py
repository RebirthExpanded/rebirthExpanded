"""Scatterbug (ME3 7 -- JP M3 007; English POR/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e81b2069-40e3-5fbe-9afa-bef3a71d6114",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name",
    display_name="Scatterbug",
    searchable_by=["Scatterbug", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=664,
    abilities=[
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
