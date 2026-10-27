"""Billy & O'Nare (SV09 142 -- JP SVP 170; English JTG/142). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def billy_and_onare(ctx):
    await ctx.draw_cards(2)
    if len(ctx.hand()) >= 10:
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="9050282a-06a5-53ad-ab2e-470e676f9f48",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillyONare.Name",
    display_name="Billy & O'Nare",
    searchable_by=["Billy & O'Nare", "Supporter"],
    subtypes=["Supporter"],
    collector_number=142,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=billy_and_onare,
)
