"""Red Card (JP XY Hyper Metal Chain Deck 60 -- HMC 012/018; English print
XY 124/146).

Item.

  "Your opponent shuffles their hand into their deck and draws 4 cards."

BANNED in Expanded like the XY print (formats.json names HMC/12).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef


async def red_card(ctx):
    await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
    await ctx.draw_cards(4, ctx.opponent_id)


card = ItemCardDef(
    guid="2d0a25b9-6653-5d17-828d-2f7e515acae6",
    key="HMC",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedCard.Name",
    display_name="Red Card",
    searchable_by=["Red Card", "Item"],
    subtypes=["Item"],
    collector_number=12,
    set_code="HMC",
    rarity=Rarities.Uncommon,
    effect=red_card,
)
