"""Exeggcute (ME1 4 -- JP M1L 004; English MEG/4). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


card = PokemonCardDef(
    guid="852545ab-cb40-5ac9-ab20-1cd950fd5976",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    display_name="Exeggcute",
    searchable_by=["Exeggcute", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=102,
    abilities=[
        Attack(
            title="Jam-Packed",
            game_text="Search your deck for a Basic Grass Energy card and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_attach_energy(_basic_grass, count=1, to_self=True, prompt="Choose a Basic Grass Energy card to attach to this Pokémon."),
        ),
    ],
)
