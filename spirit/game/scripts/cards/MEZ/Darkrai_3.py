"""Darkrai (MEZ 3 -- JP MEZ 003; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_darkness(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.DARKNESS)


card = PokemonCardDef(
    guid="d1588908-6bbe-531f-90b5-c29e35599eb7",
    key="MEZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai",
    searchable_by=["Darkrai", "Basic"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="MEZ",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=491,
    abilities=[
        Attack(
            title="Shadow Veil",
            game_text="Search your deck for up to 2 Basic Darkness Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=su.search_attach_energy(_basic_darkness, count=2, to_self=True, prompt="Choose up to 2 Basic Darkness Energy cards to attach to this Pokémon."),
        ),
        Attack(
            title="Dark Cutter",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
