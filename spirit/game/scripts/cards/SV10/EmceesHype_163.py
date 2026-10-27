"""Emcee's Hype (SV10 163 -- JP M6 067; English DRI/163, DRI/220). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects import attacks_common as ac


async def emcees_hype(ctx):
    await ctx.draw_cards(2)
    if ac.count_prizes_remaining("opponent")(ctx) <= 3:
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="aa7d0e3d-3dfd-5755-a8ef-321d87ea4559",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EmceesHype.Name",
    display_name="Emcee's Hype",
    searchable_by=["Emcee's Hype", "Supporter"],
    subtypes=["Supporter"],
    collector_number=163,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    effect=emcees_hype,
)
