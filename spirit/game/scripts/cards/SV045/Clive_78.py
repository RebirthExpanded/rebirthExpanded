"""Clive (SV045 78 -- JP SV4a 175; English PAF/227, PAF/236, PAF/78). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.session.effects import is_supporter_card


async def clive(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    n = sum(1 for c in hand if is_supporter_card(c))
    if n:
        await ctx.draw_cards(2 * n)


card = SupporterCardDef(
    guid="540bee61-efd2-5641-a61e-4d4fc0e822b4",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clive.Name",
    display_name="Clive",
    searchable_by=["Clive", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=clive,
)
