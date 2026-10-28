"""Parasol Lady (SV4 169 -- JP SV3a 061; English PAR/169, PAR/238, PAR/255). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def parasol_lady(ctx):
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.player_id)
    else:
        await ctx.shuffle_deck()
    going_second = ctx.player_id != ctx.session.first_player_id
    await ctx.draw_cards(8 if going_second and ctx.session.turn_state.turn_number == 2 else 4)


card = SupporterCardDef(
    guid="2a57787e-22a1-5d9f-90cf-3f160f047803",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ParasolLady.Name",
    display_name="Parasol Lady",
    searchable_by=["Parasol Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=169,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    effect=parasol_lady,
)
