"""Foongus (SV3 9 -- JP SV1a 002; English OBF/9). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])

from spirit.game.session.effects import is_basic_pokemon


def _basic_grass_mon(card) -> bool:
    return is_basic_pokemon(card) and _of_type(card, PokemonTypes.GRASS)


card = PokemonCardDef(
    guid="de7febf2-62cf-50cf-8ff8-8cee79a509a0",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    display_name="Foongus",
    searchable_by=["Foongus", "Basic"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=590,
    abilities=[
        Attack(
            title="Enticing Pattern",
            game_text="Search your deck for a Basic Grass Pokémon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=su.search_to_bench(_basic_grass_mon, count=1, prompt="Choose a Basic Grass Pokémon."),
        ),
        Attack(
            title="Beat",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
