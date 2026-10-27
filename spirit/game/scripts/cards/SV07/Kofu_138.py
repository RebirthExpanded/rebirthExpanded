"""Kofu (SV07 138 -- JP SV7 099; English SCR/138, SCR/165). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

def _two_others(board, player_id, card=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len([c for c in hand.children if c is not card]) >= 2


async def kofu(ctx):
    pool = [c for c in ctx.hand() if c is not ctx.source]
    if len(pool) < 2:
        return
    picks = await ctx.choose_cards(pool, 2, minimum=2, prompt="Choose 2 cards to put on the bottom of your deck")
    if len(picks) < 2:
        return
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)
    await ctx.draw_cards(4)


card = SupporterCardDef(
    guid="7b719380-b8c3-5531-aaac-491dd5d4ee45",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kofu.Name",
    display_name="Kofu",
    searchable_by=["Kofu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=_two_others,
    effect=kofu,
)
