"""Colress (BW - Plasma Storm 118/135 -- JP BW7-B 064/070).

Supporter.

  "Shuffle your hand into your deck. Then, draw a number of cards equal to
   the number of Benched Pokemon (both yours and your opponent's)."

Cynthia with the draw counted off both Benches at the moment of drawing.
(Kyurem's Trifrost reads this card's name in the discard pile for its
Energy discount; nothing else here.)
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef


async def colress(ctx):
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    count = len(ctx.my_bench()) + len(ctx.opponent_bench())
    if count > 0:
        await ctx.draw_cards(count)


card = SupporterCardDef(
    guid="4380e216-ec40-5790-8617-01410ce59676",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Colress.Name",
    display_name="Colress",
    searchable_by=["Colress", "Supporter"],
    subtypes=["Supporter"],
    collector_number=118,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=colress,
)
