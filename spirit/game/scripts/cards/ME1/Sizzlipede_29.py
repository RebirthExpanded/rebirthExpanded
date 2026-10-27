"""Sizzlipede (ME1 29 -- JP M1S 012; English MEG/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="b7b37617-14a5-5d28-9152-83debc980653",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    display_name="Sizzlipede",
    searchable_by=["Sizzlipede", "Basic"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=850,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
