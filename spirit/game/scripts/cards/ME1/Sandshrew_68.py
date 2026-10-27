"""Sandshrew (ME1 68 -- JP M1L 020; English MEG/68). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="d7f8835b-0566-5a84-a041-deb4073a31fb",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    display_name="Sandshrew",
    searchable_by=["Sandshrew", "Basic"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=27,
    abilities=[
        Attack(
            title="Dig Claws",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Mud-Slap",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
