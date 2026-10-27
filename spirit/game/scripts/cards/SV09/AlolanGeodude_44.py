"""Alolan Geodude (SV09 44 -- JP SVM 039; English JTG/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="ff0f0d80-1e2c-512a-9ac6-049e790979d7",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name",
    display_name="Alolan Geodude",
    searchable_by=["Alolan Geodude", "Basic"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=74,
    abilities=[
        Attack(
            title="Knuckle Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Tiny Charge",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
