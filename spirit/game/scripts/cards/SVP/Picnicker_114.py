"""Picnicker (SVP 114 -- JP SVI 065; English SVP/114). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def picnicker(ctx):
    results = await ctx.flip_coins(1, "Picnicker")
    await ctx.draw_cards(4 if results and results[0] else 2)


card = SupporterCardDef(
    guid="d12c52fb-83bf-554e-9586-e0d7c4cefe7f",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Picnicker.Name",
    display_name="Picnicker",
    searchable_by=["Picnicker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=114,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    effect=picnicker,
)
