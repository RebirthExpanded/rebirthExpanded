"""Nosepass (ME3 37 -- JP M3 036; English POR/37). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="509ca1db-24de-5951-a6f2-3715e0f06b5a",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    display_name="Nosepass",
    searchable_by=["Nosepass", "Basic"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=299,
    abilities=[
        Attack(
            title="Rolling Rocks",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
        ),
    ],
)
