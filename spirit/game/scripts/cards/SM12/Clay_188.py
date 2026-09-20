"""Clay (SM - Cosmic Eclipse 188/236 -- JP SM12 095/095, the art here).

Supporter.

  "Discard the top 7 cards of your deck. Then, put any number of Item
   cards you discarded in this way into your hand."

The Items go to the hand off the discard pile, so a discard trigger that
watches the pile (Slime Mold Colony and the like) sees them land first.
"Any number" is the player's pick, and the Items are shown on the way up
-- put_in_hand's reveal -- because the opponent watched them being milled
and gets to see which ones came back.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import is_item_card

MILL = 7


async def clay(ctx):
    top = ctx.deck_top(MILL)
    if not top:
        return
    await ctx.discard_cards(top)
    items = [c for c in top if is_item_card(c)]
    if not items:
        return
    keep = await ctx.choose_cards(
        items, count=len(items), minimum=0,
        prompt="Choose any number of Item cards to put into your hand.")
    if keep:
        await ctx.put_in_hand(keep, reveal=True)


card = SupporterCardDef(
    guid="1cdeee82-aac8-50f9-bacc-9354fbf6bd47",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clay.Name",
    display_name="Clay",
    searchable_by=["Clay", "Supporter"],
    subtypes=["Supporter"],
    collector_number=188,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=clay,
)
