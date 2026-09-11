"""Revitalizer (XY - Generations 70/83 -- JP XY-P promo).

Item.

  "Put 2 Grass Pokémon from your discard pile into your hand."

Any stage, any two; playable with at least one there, and with only
one it takes the one.
"""

from spirit.game.attributes import Rarities
from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.support_common import (recover_from_discard,
                                                      requires_discard)
from spirit.game.session.effects import is_pokemon_of_type


def _is_grass_pokemon(card):
    return is_pokemon_of_type(card, PokemonTypes.GRASS)

from spirit.game.data_utils import ItemCardDef

card = ItemCardDef(
    guid="814a41de-6add-52b0-9402-62e3faa64042",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revitalizer.Name",
    display_name="Revitalizer",
    searchable_by=["Revitalizer", "Item", "Revitalizer"],
    subtypes=["Item"],
    collector_number=70,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(
        _is_grass_pokemon, count=2, minimum=1,
        prompt="Choose up to 2 Grass Pokémon to put into your hand."),
    condition=requires_discard(_is_grass_pokemon, 1),
)
