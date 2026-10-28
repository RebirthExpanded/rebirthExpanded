"""Dendra (SV2 179 -- JP SV1a 066; English PAL/179, PAL/250, PAL/266). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

def _another_card(board, player_id, card=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len([c for c in hand.children if c is not card]) >= 1


async def dendra(ctx):
    pool = [c for c in ctx.hand() if c is not ctx.source]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Put a card from your hand on the bottom of your deck")
    if picks:
        await ctx.put_on_bottom_of_deck(picks[0])
        await ctx.draw_until(5)


card = SupporterCardDef(
    guid="37d8e044-66a0-5367-a632-13d4b0cf5ca2",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dendra.Name",
    display_name="Dendra",
    searchable_by=["Dendra", "Supporter"],
    subtypes=["Supporter"],
    collector_number=179,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_another_card,
    effect=dendra,
)
