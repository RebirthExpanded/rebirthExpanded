"""Order Pad (SM - Ultra Prism 131/156 -- JP SM5M 053/066).

Item.

  "Flip a coin. If heads, search your deck for an Item card, reveal it,
   and put it into your hand. Then, shuffle your deck."

Roller Skates' shape with a search instead of a draw: the coin first, and
only heads opens the deck. The empty-deck gate keeps it off the panel
when there is nothing to search at all, so the flip is never spent on
nothing.

It finds an ITEM, which under this pool's rule that a Pokemon Tool is
never an Item means a Float Stone is not among the candidates.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_item_card

card = ItemCardDef(
    guid="fe783245-5407-506e-a863-1b4fa5c58735",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OrderPad.Name",
    display_name="Order Pad",
    searchable_by=["Order Pad", "Item", "OrderPad"],
    subtypes=["Item"],
    collector_number=131,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=flip_or_nothing(then=search_to_hand(
        is_item_card, count=1, minimum=0,
        prompt="Choose an Item card to put into your hand.")),
)
