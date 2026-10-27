"""Swinub (ME2 23 -- JP M2 023; English PFL/23). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="b90175b8-cebb-5211-b4a4-7f14bd3998de",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    display_name="Swinub",
    searchable_by=["Swinub", "Basic"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=220,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Icy Snow",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
