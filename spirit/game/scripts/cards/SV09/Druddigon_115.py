"""Druddigon (SV09 115 -- JP SV9 073; English JTG/115). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)



def _dragon(pokemon) -> bool:
    return PokemonTypes.DRAGON.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="8db20130-f3ab-5a89-8e80-2297024e9870",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon", "Basic"],
    subtypes=["Basic"],
    collector_number=115,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=621,
    abilities=[
        Attack(
            title="Dragon's Fury",
            game_text="Attach a Basic Fire Energy card from your discard pile to 1 of your Dragon Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.attach_from_discard(_basic_fire, count=1, target=_dragon, minimum=0, prompt="Attach a Basic Fire Energy card to 1 of your Dragon Pokémon."),
        ),
        Attack(
            title="Slashing Claw",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
