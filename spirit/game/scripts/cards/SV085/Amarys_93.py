"""Amarys (SV085 93 -- JP SV8a 173; English PRE/132, PRE/170, PRE/93). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def amarys(ctx):
    await ctx.draw_cards(4)
    owner = ctx.player_id

    async def _end(session):
        from spirit.game.session.effects import EffectContext
        c = EffectContext(session, owner, None, None)
        hand = list(c.hand(owner))
        if len(hand) >= 5:
            await c.discard_cards(hand)
            await c.flush_choreography()

    ctx.schedule_at_checkup(0, _end)


card = SupporterCardDef(
    guid="570e9c0b-71e9-5936-9a63-b779f69331e9",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Amarys.Name",
    display_name="Amarys",
    searchable_by=["Amarys", "Supporter"],
    subtypes=["Supporter"],
    collector_number=93,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=amarys,
)
