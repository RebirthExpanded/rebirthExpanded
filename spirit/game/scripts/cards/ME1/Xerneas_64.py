"""Xerneas (ME1 64 -- JP M1S 046; English MEG/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.effects import is_basic_pokemon


def _basic_psychic(card) -> bool:
    return is_basic_pokemon(card) and PokemonTypes.PSYCHIC.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="5b1c434d-26ae-55d2-a03c-ac420c56d8e4",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=716,
    abilities=[
        Attack(
            title="Geo Gate",
            game_text="Search your deck for up to 3 Basic Psychic Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=su.search_to_bench(_basic_psychic, count=3, prompt="Choose up to 3 Basic Psychic Pokémon."),
        ),
        Attack(
            title="Bright Horns",
            game_text="During your next turn, this Pokémon can't use Bright Horns.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)
