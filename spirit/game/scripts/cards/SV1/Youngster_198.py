"""Youngster (SV1 198 -- JP SVAL 019; English SVI/198). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def youngster(ctx):
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.player_id)
    else:
        await ctx.shuffle_deck()
    await ctx.draw_cards(5)


card = SupporterCardDef(
    guid="ba7d5b1d-90a4-5b06-b69d-637dbba26d56",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Youngster.Name",
    display_name="Youngster",
    searchable_by=["Youngster", "Supporter"],
    subtypes=["Supporter"],
    collector_number=198,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=youngster,
)
