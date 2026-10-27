"""Heatmor (RSV10PT5 19 -- JP SV11W 016; English WHT/104, WHT/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)



def _fire_pick(card) -> bool:
    return _basic_fire(card) or (is_pokemon_card(card) and _of_type(card, PokemonTypes.FIRE))


card = PokemonCardDef(
    guid="bb8d545f-1392-5581-91c2-0fa87ed0f9d4",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Licking Catch",
            game_text="Search your deck for up to 3 in any combination of Fire Pokémon and Basic Fire Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=su.search_to_hand(_fire_pick, count=3, reveal=True, prompt="Choose up to 3 Fire Pokémon and Basic Fire Energy cards."),
        ),
        Attack(
            title="Fire Claws",
            game_text="",
            cost={PokemonTypes.FIRE: 2},
            damage=60,
        ),
    ],
)
