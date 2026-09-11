"""Recycle (BW - Emerging Powers 96/98 -- JP BW1-Bb 052/053, the art here).

Item.

  "Flip a coin. If heads, put a card from your discard pile on top of your
   deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.data_utils import ItemCardDef


async def recycle(ctx):
    heads = await ctx.flip_coins(1, "Recycle")
    if not (heads and heads[0]):
        return
    cards = list(ctx.discard_pile())
    picks = await ctx.choose_cards(
        cards, 1, minimum=1, prompt="Choose a card to put on top of your deck")
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.put_on_top_of_deck(picks[0])


card = ItemCardDef(
    guid="a0dddc91-ae6e-582c-b74d-b5753620362c",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Recycle.Name",
    display_name="Recycle",
    searchable_by=["Recycle", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    condition=requires_discard(None, 1),
    effect=recycle,
)
