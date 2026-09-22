"""Xtransceiver (BW - Noble Victories 96/101 -- JP BW2 061/066, the art here).

Item.

  "Flip a coin. If heads, search your deck for a Supporter card, reveal
   it, and put it into your hand. Shuffle your deck afterward."

Tails ends it before the browser opens; the deck is only shuffled when
it was searched.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_supporter_card


async def xtransceiver(ctx):
    if not (await ctx.flip_coins(1, "Xtransceiver"))[0]:
        return
    picks = await ctx.search_deck(
        is_supporter_card, count=1, minimum=0,
        prompt="Choose a Supporter card to put into your hand.")
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="bbbb9877-289a-50b5-81f4-86a93664c491",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Xtransceiver.Name",
    display_name="Xtransceiver",
    searchable_by=["Xtransceiver", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=xtransceiver,
)
