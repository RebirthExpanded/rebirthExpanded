"""Surprise Box (SM - Unbroken Bonds 187/214 -- JP SM9a 044/055, the art here).

Item.

  "Put a card from your opponent's discard pile into their hand."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef


def _condition(board, player_id, pokemon=None) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    pile = board.find_player_area(opponent, "discard") if opponent else None
    return bool(pile) and bool(pile.children)


async def surprise_box(ctx):
    cards = list(ctx.discard_pile(ctx.opponent_id))
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=1, prompt="Choose a card from your opponent's discard pile to put into their hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = ItemCardDef(
    guid="e7aa096b-ad0d-5b0d-8acb-f3c14592563a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurpriseBox.Name",
    display_name="Surprise Box",
    searchable_by=["Surprise Box", "Item", "SurpriseBox"],
    subtypes=["Item"],
    collector_number=187,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=_condition,
    effect=surprise_box,
)
