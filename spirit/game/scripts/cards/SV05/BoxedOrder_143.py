"""Boxed Order (SV - Temporal Forces 143/162 -- JP SV5K 061/071).

Item.

  "Search your deck for up to 2 Item cards, reveal them, and put them into
   your hand. Then, shuffle your deck. Your turn ends."

Order Pad's two-card cousin with no coin and a price: the turn ends the
moment it resolves, which ctx.ends_turn carries the way Steven's Resolve
and Boost Shake do.

The printed order is search first, turn ends second, so the cards do reach
your hand -- there is simply nothing left to do with them until next turn.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_item_card


async def boxed_order(ctx):
    """Two Items out of the deck, and that is the turn."""
    await search_to_hand(
        is_item_card, count=2, minimum=0,
        prompt="Choose up to 2 Item cards to put into your hand.")(ctx)
    ctx.ends_turn = True


card = ItemCardDef(
    guid="183ffac5-224c-58fe-abca-25274d26c148",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BoxedOrder.Name",
    display_name="Boxed Order",
    searchable_by=["Boxed Order", "Item", "BoxedOrder"],
    subtypes=["Item"],
    collector_number=143,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=boxed_order,
)
