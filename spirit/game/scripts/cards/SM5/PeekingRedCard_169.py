"""Peeking Red Card (SM - Crimson Invasion 97/111 -- JP SM4S 047/050).

Item.

  "Look at your opponent's hand. You may have your opponent shuffle their
   hand into their deck. If you do, your opponent draws a card for each
   card they shuffled into their deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef


async def peeking_red_card(ctx):
    opp = ctx.opponent_id
    hand = await ctx.reveal_hand(of_player=opp, to_player=ctx.player_id)
    if not hand:
        return
    if not await ctx.ask_yes_no(
            "Have your opponent shuffle their hand into their deck and draw that many cards?"):
        return
    count = len(ctx.hand(opp))
    await ctx.shuffle_into_deck(ctx.hand(opp), opp)
    await ctx.draw_cards(count, opp)


card = ItemCardDef(
    guid="a6084b29-e8d0-5287-93c4-1d2c316dfec4",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PeekingRedCard.Name",
    display_name="Peeking Red Card",
    searchable_by=["Peeking Red Card", "Item", "PeekingRedCard"],
    subtypes=["Item"],
    collector_number=169,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    effect=peeking_red_card,
)
