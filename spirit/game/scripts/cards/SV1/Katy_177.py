"""Katy (SV1 177 -- JP SV1V 074; English SVI/177, SVI/237). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def katy(ctx):
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.player_id)
    else:
        await ctx.shuffle_deck()
    await ctx.draw_cards(8)
    ctx.ends_turn = True


card = SupporterCardDef(
    guid="884caf0a-98e7-53f7-a253-c5b064fe98a3",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Katy.Name",
    display_name="Katy",
    searchable_by=["Katy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=katy,
)
