"""Dive Ball (XY - Primal Clash 125/160 -- JP XY5 043/060).

Item.

  "Search your deck for a Water Pokemon, reveal it, and put it into your
   hand. Shuffle your deck afterward."

Any stage: a Blastoise is as good a target as a Squirtle. The type is the
card's printed [W], which is what is_water_pokemon reads.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_water_pokemon

card = ItemCardDef(
    guid="05c90989-fc76-5df5-9483-66b4761201c9",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DiveBall.Name",
    display_name="Dive Ball",
    searchable_by=["Dive Ball", "Item", "DiveBall"],
    subtypes=["Item"],
    collector_number=125,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        is_water_pokemon, count=1, minimum=0,
        prompt="Choose a Water Pokémon to put into your hand."),
)
