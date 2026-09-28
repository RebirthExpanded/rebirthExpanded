"""Lt. Surge's Bargain (ME - Mega Evolution 120/132 -- JP M1L 061/063).

Supporter.

  "Ask your opponent if each player may take a Prize card. If yes, each
   player takes a Prize card. If no, you draw 4 cards."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef


async def lt_surges_bargain(ctx):
    opp = ctx.opponent_id
    if await ctx.ask_yes_no("Your opponent asks: may each player take a Prize card?",
                            player_id=opp):
        await ctx.flush_choreography()
        await ctx.session._take_prizes(ctx.player_id, 1)
        await ctx.session._take_prizes(opp, 1)
    else:
        await ctx.draw_cards(4)


card = SupporterCardDef(
    guid="1f85c255-b67a-530a-9d8d-009ecb4c9484",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesBargain.Name",
    display_name="Lt. Surge's Bargain",
    searchable_by=["Lt. Surge's Bargain", "Supporter", "LtSurgesBargain"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=lt_surges_bargain,
)
