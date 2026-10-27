"""Articuno (SV09 32 -- JP SV9 018; English JTG/161, JTG/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)


card = PokemonCardDef(
    guid="ae0da7e7-8610-5f92-8754-a4f1463a8bc1",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=144,
    abilities=[
        Attack(
            title="Frigid Fluttering",
            game_text="Search your deck for up to 2 Basic Water Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_attach_energy(_basic_water, count=2, to_self=True, prompt="Choose up to 2 Basic Water Energy cards to attach to this Pokémon."),
        ),
        Attack(
            title="Ice Blast",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
