"""Cresselia (ME2 39 -- JP MBD 003; English PFL/39). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_psychic(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.PSYCHIC)


card = PokemonCardDef(
    guid="135c6570-210b-551e-aef7-2839c8e753dd",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    display_name="Cresselia",
    searchable_by=["Cresselia", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=488,
    abilities=[
        Attack(
            title="Swelling Light",
            game_text="Search your deck for up to 2 Basic Psychic Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=su.search_attach_energy(_basic_psychic, count=2, to_self=True, prompt="Choose up to 2 Basic Psychic Energy cards to attach to this Pokémon."),
        ),
        Attack(
            title="Aurora Beam",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)
