"""Koko (SPJ 106 -- JP SP 106; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su

from spirit.game.attributes import PokemonTypes
from spirit.game.session.effects import is_pokemon_of_type


def _grass_pokemon(card):
    return is_pokemon_of_type(card, PokemonTypes.GRASS)


card = PokemonCardDef(
    guid="c6035aa5-1479-5a96-be3c-421477e3f6e3",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koko.Name",
    display_name="Koko",
    searchable_by=["Koko", "Basic"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SPJ",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=893,
    abilities=[
        Attack(
            title="Forest Call",
            game_text="Search your deck for a Grass Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(_grass_pokemon, count=1, reveal=True, prompt="Choose a Grass Pokémon."),
        ),
        Attack(
            title="Tarzan Kick",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
