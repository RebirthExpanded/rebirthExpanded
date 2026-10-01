"""Puzzle of Time (XY - BREAKpoint 109/122 -- JP XY9 071/080).

Item.

  "You may play 2 Puzzle of Time cards at once.
   - If you played 1 card, look at the top 3 cards of your deck and put
     them back in any order.
   - If you played 2 cards, put 2 cards from your discard pile into your
     hand."

Banned in Expanded (formats.json already lists XY9/109).

Custom Catcher's shape: the client plays one card at a time, so "2 at
once" is asked when the first resolves. With a second copy in hand and a
card in the discard pile that may go to the hand, the player picks; the
two-card mode plays the second copy out of the hand as part of the same
effect. Neither Puzzle being played can be taken back by it, and a card
that can't leave the discard pile for the hand (Neutralization Zone) is
never offered.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.session.effects import stuck_in_discard

NAME = "Puzzle of Time"


def _is_puzzle(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == NAME


def _area(board, player_id, name):
    area = board.find_player_area(player_id, name)
    return list(area.children) if area else []


def _can_play(board, player_id, card=None) -> bool:
    """One card: something in the deck to look at. Two: another copy in
    hand and a card in the discard pile that may go to the hand."""
    if _area(board, player_id, "deck"):
        return True
    others = [c for c in _area(board, player_id, "hand") if c is not card]
    return (any(_is_puzzle(c) for c in others)
            and any(not stuck_in_discard(c) for c in _area(board, player_id, "discard")))


async def puzzle_of_time(ctx):
    second = next((c for c in ctx.hand() if _is_puzzle(c)), None)
    pool = [c for c in ctx.recoverable_discard() if c is not ctx.source]
    choice = 0
    if second is not None and pool:
        if not ctx.deck():
            choice = 1
        else:
            choice = await ctx.choose(
                "Puzzle of Time: play 1 or 2?",
                ["Play 1: look at the top 3 cards of your deck",
                 "Play 2: put 2 cards from your discard pile into your hand"])
    if choice == 1:
        await ctx.discard_cards([second])
        ctx.session._record_trainer_played(second)
        pool = [c for c in pool if c is not second]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, min(2, len(pool)), minimum=min(2, len(pool)),
            prompt="Choose 2 cards to put into your hand.")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        return
    await ctx.reorder_deck_top(3)


card = ItemCardDef(
    guid="f9bdcf05-6e3e-5dce-8d23-cb767f4d3f2c",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PuzzleofTime.Name",
    display_name="Puzzle of Time",
    searchable_by=["Puzzle of Time", "Item", "PuzzleofTime"],
    subtypes=["Item"],
    collector_number=109,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    condition=_can_play,
    effect=puzzle_of_time,
)
