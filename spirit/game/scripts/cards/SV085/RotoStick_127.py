"""Roto-Stick (SV - Prismatic Evolutions 127/131 -- JP SV-P 160, the art here).

Item.

  "Look at the top 4 cards of your deck. You may reveal any number of
   Supporter cards you find there and put them into your hand. Shuffle
   the other cards back into your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_supporter_card


async def roto_stick(ctx):
    top = ctx.deck_top(4)
    if not top:
        return
    supporters = [c for c in top if is_supporter_card(c)]
    picks = await ctx.choose_cards(
        supporters, max(len(supporters), 1), minimum=0,
        prompt="Choose any number of Supporter cards to put into your hand",
        display_cards=top if len(supporters) < len(top) else None)
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="7d695632-a1f1-58ba-92b3-48f2f6035e97",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotoStick.Name",
    display_name="Roto-Stick",
    searchable_by=["Roto-Stick", "Item", "RotoStick"],
    subtypes=["Item"],
    collector_number=127,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=requires_deck(1),
    effect=roto_stick,
)
