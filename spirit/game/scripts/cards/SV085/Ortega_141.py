"""Ortega (SV085 141 -- JP SV3 104; English OBF/190, OBF/219, PRE/141). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def ortega(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    picks = await ctx.choose_cards(hand, 1, minimum=1, prompt="Choose a card to put on the bottom of their deck")
    if picks and await ctx.put_on_bottom_of_deck(picks[0]):
        if await ctx.ask_yes_no("Draw a card?", player_id=ctx.opponent_id):
            await ctx.draw_cards(1, player_id=ctx.opponent_id)


card = SupporterCardDef(
    guid="fb45112e-aa3e-5885-ba26-c43ccc9d17c1",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ortega.Name",
    display_name="Ortega",
    searchable_by=["Ortega", "Supporter"],
    subtypes=["Supporter"],
    collector_number=141,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareUltra,
    effect=ortega,
)
