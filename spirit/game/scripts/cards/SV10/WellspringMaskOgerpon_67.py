"""Wellspring Mask Ogerpon (SV10 67 -- JP SV9a 033; English DRI/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)
from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="c8cefc02-b6a3-57e3-ad72-e3c6bb968867",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WellspringMaskOgerpon.Name",
    display_name="Wellspring Mask Ogerpon",
    searchable_by=["Wellspring Mask Ogerpon", "Basic"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=1017,
    abilities=[
        Attack(
            title="Water Kagura",
            game_text="Search your deck for a Basic Water Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_attach_energy(_basic_water, count=1, prompt="Choose a Basic Water Energy card to attach to 1 of your Pokémon."),
        ),
        Attack(
            title="Bubble Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=su.heal_attack(30),
        ),
    ],
)
