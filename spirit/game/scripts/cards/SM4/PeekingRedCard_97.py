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
    guid="258ec1e2-83e9-5ba7-b307-458f97496752",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PeekingRedCard.Name",
    display_name="Peeking Red Card",
    searchable_by=["Peeking Red Card", "Item", "PeekingRedCard"],
    subtypes=["Item"],
    collector_number=97,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    effect=peeking_red_card,
)
