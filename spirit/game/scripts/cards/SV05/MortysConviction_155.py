"""Morty's Conviction (SV05 155 -- JP SV5K 069; English TEF/155, TEF/201, TEF/211). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

def _another_card(board, player_id, card=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len([c for c in hand.children if c is not card]) >= 1


async def mortys_conviction(ctx):
    paid = await ctx.discard_from_hand(1, minimum=1, exclude=[ctx.source],
                                       prompt="Discard a card from your hand to use Morty's Conviction.")
    n = len(ctx.opponent_bench())
    if paid and n:
        await ctx.draw_cards(n)


card = SupporterCardDef(
    guid="009c299e-463a-57aa-a128-25de294c0eeb",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MortysConviction.Name",
    display_name="Morty's Conviction",
    searchable_by=["Morty's Conviction", "Supporter"],
    subtypes=["Supporter"],
    collector_number=155,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=_another_card,
    effect=mortys_conviction,
)
