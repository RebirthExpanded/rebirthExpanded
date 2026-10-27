"""Drasna (SV08 173 -- JP SV7a 062; English SSP/173, SSP/231). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def drasna(ctx):
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.player_id)
    else:
        await ctx.shuffle_deck()
    results = await ctx.flip_coins(1, "Drasna")
    await ctx.draw_cards(8 if results and results[0] else 3)


card = SupporterCardDef(
    guid="a0c0780f-4c4f-5ae0-aa61-c5eb0b51428a",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Drasna.Name",
    display_name="Drasna",
    searchable_by=["Drasna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=drasna,
)
