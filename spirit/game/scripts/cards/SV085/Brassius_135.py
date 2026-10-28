"""Brassius (SV085 135 -- JP SV8a 190; English OBF/187, PRE/135). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def brassius(ctx):
    hand = [c for c in ctx.hand() if c is not ctx.source]
    n = len(hand)
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.player_id)
    else:
        await ctx.shuffle_deck()
    await ctx.draw_cards(n + 1)


card = SupporterCardDef(
    guid="e23ae435-2758-51cc-bb54-a812adc6beb9",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brassius.Name",
    display_name="Brassius",
    searchable_by=["Brassius", "Supporter"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareUltra,
    effect=brassius,
)
