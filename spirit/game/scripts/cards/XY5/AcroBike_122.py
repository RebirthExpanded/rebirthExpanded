"""Acro Bike (XY - Primal Clash 122/160).

Item.

  "Look at the top 2 cards of your deck and put 1 of them into your hand.
   Discard the other card."

Air Mail's shape with the other card discarded instead of buried, so it
shares nothing but the look: the pick is mandatory, and with a single card
left in the deck that card is the whole choice and nothing is discarded.
"""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_deck


async def acro_bike(ctx):
    """Top 2: one to hand, the other to the discard pile."""
    top = ctx.deck_top(2)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1, prompt="Choose 1 of the top 2 cards to put into your hand.",
        display_cards=top,
    )
    if not picks:
        return
    chosen = picks[0]
    await ctx.put_in_hand([chosen], reveal=False)
    rest = [c for c in top if c is not chosen]
    if rest:
        await ctx.discard_cards(rest)


card = ItemCardDef(
    guid="f72ce6a9-0dcb-5776-b08d-a6b1975faef9",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcroBike.Name",
    display_name="Acro Bike",
    searchable_by=["Acro Bike", "Item", "AcroBike"],
    subtypes=["Item"],
    collector_number=122,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=acro_bike,
    condition=requires_deck(),
)
