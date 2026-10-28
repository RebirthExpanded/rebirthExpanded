"""Ryme (SV3 194 -- JP SV3 106; English OBF/194, OBF/221). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects import support_common as su


async def ryme(ctx):
    await ctx.draw_cards(3)
    await su.opponent_switches(ctx)


card = SupporterCardDef(
    guid="b3df55eb-2828-5e1b-9ec0-1dc09c8bc70a",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ryme.Name",
    display_name="Ryme",
    searchable_by=["Ryme", "Supporter"],
    subtypes=["Supporter"],
    collector_number=194,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    effect=ryme,
)
