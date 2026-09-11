"""Fiery Flint (SM - Dragon Majesty 60/70 -- JP SM6a 052/053).

Item.

  "You can play this card only if you discard 2 other cards from your hand. Search your deck for up to 4 Fire Energy cards, reveal them, and put them into your hand. Then, shuffle your deck."

Ultra Ball's shape: the two discards are the price and are paid first,
and the card is only offered with 2 OTHER cards to pay with. Fire Energy
is the printed [R], so a Special Energy that merely provides [R] is not a
target.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import fiery_flint
from spirit.game.data_utils import ItemCardDef

card = ItemCardDef(
    guid="e47f8609-a282-52f0-aec1-22da1a678b80",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieryFlint.Name",
    display_name="Fiery Flint",
    searchable_by=["Fiery Flint", "Item", "FieryFlint"],
    subtypes=["Item"],
    collector_number=60,
    set_code="DM",
    rarity=Rarities.Uncommon,
    effect=fiery_flint,
    condition=requires_hand(None, 2),
)
