"""Litleo (ME1 23 -- JP M1S 010; English MEG/139, MEG/23). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="fb3f301c-1419-5dd2-aa3a-0c0c438c7fae",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    display_name="Litleo",
    searchable_by=["Litleo", "Basic"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=667,
    abilities=[
        Attack(
            title="Flare",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
