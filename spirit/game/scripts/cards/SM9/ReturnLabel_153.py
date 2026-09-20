"""Return Label (SM - Team Up 153/181 -- JP SM-P 235, the art here).

Item.

  "Put a card from your opponent's discard pile on the bottom of their
   deck."

The pick is shown to the opponent on the way (the printed JP text says
so; the pile is public anyway). Playable only with a card in their
discard pile.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef


def _opponent_discard_not_empty(board, player_id) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    pile = board.find_player_area(opponent, "discard") if opponent else None
    return bool(pile and pile.children)


async def return_label(ctx):
    pile = ctx.discard_pile(ctx.opponent_id)
    if not pile:
        return
    picks = await ctx.choose_cards(
        pile, 1, minimum=1,
        prompt="Choose a card from your opponent's discard pile to put on the bottom of their deck.")
    if picks:
        await ctx.reveal_cards(picks, to_player=ctx.opponent_id)
        await ctx.put_on_bottom_of_deck(picks[0])


card = ItemCardDef(
    guid="c8cddee4-0f79-5898-a07f-d472cd28e5e8",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReturnLabel.Name",
    display_name="Return Label",
    searchable_by=["Return Label", "Item", "ReturnLabel"],
    subtypes=["Item"],
    collector_number=153,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    condition=_opponent_discard_not_empty,
    effect=return_label,
)
