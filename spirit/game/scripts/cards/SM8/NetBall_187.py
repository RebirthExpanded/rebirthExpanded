"""Net Ball (SM - Lost Thunder 187/214 -- JP SM7b 057/066).

Item.

  "Search your deck for a Basic Grass Pokemon or a Grass Energy card,
   reveal it, and put it into your hand. Then, shuffle your deck."

Either half of the "or" is a candidate, so the search offers Basic Grass
Pokemon and [G] Energy together and takes one. BASIC Grass Pokemon only --
a Decidueye in the deck is not a target -- and the Energy clause reads the
printed [G] symbol, so a Grass-typed basic Energy qualifies and a Special
Energy that merely provides [G] does not.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_grass_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_basic_pokemon, is_pokemon_of_type


def _basic_grass_or_grass_energy(card) -> bool:
    return (
        (is_basic_pokemon(card) and is_pokemon_of_type(card, PokemonTypes.GRASS))
        or is_grass_energy_card(card)
    )


card = ItemCardDef(
    guid="3229b67c-b1b8-5e14-a8d2-46f2f766b933",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NetBall.Name",
    display_name="Net Ball",
    searchable_by=["Net Ball", "Item", "NetBall"],
    subtypes=["Item"],
    collector_number=187,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _basic_grass_or_grass_energy, count=1, minimum=0,
        prompt="Choose a Basic Grass Pokémon or a Grass Energy card."),
)
