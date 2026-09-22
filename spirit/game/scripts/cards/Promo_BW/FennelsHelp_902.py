"""Fennel's Help (JP WAK 047/047, Everyone's Exciting Battle -- JP only).

Supporter. No English print, so it carries a pool-local number.

  "Flip a coin until you get tails. Draw 2 cards for each heads."

One coin screen shows the whole run (flip_until_tails), then the draw.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

PER_HEADS = 2


async def fennels_help(ctx):
    heads = await ctx.flip_until_tails("Fennel's Help")
    if heads:
        await ctx.draw_cards(PER_HEADS * heads)


card = SupporterCardDef(
    guid="a9c398cf-0c2e-52cb-b75e-1b1dc623ed9f",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FennelsHelp.Name",
    display_name="Fennel's Help",
    searchable_by=["Fennel's Help", "Supporter", "FennelsHelp"],
    subtypes=["Supporter"],
    collector_number=902,
    set_code="Promo_BW",
    rarity=Rarities.Uncommon,
    effect=fennels_help,
)
