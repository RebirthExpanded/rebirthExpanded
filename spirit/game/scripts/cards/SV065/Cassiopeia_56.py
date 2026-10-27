"""Cassiopeia (SV065 56 -- JP SV6a 061; English SFA/56, SFA/86, SFA/94). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

def _last_card(board, player_id, card=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and all(c is card for c in hand.children) and card is not None


async def cassiopeia(ctx):
    picks = await ctx.search_deck(count=2, minimum=0, prompt="Choose up to 2 cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="9a195623-419d-55c7-a163-59e5603a27f8",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cassiopeia.Name",
    display_name="Cassiopeia",
    searchable_by=["Cassiopeia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=56,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=_last_card,
    effect=cassiopeia,
)
