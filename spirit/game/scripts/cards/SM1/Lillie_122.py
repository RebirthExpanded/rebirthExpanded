"""Lillie (SM - Sun & Moon 122/149 -- JP SM7 092/096, the art here).

Supporter.

  "Draw cards until you have 6 cards in your hand. If it's your first turn,
   draw cards until you have 8 cards in your hand."

Under current rules the player going first cannot play a Supporter on
their first turn, so "your first turn" can only be the second player's
first turn -- turn 2 of the game (house ruling; the 8-card case dates from
when the first player could). With 6 (or, then, 8) or more other cards in
hand the card is not playable at all (house ruling).
The JP SM7 reprint has no English Celestial Storm print, so the card sits
at its original Sun & Moon number.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import second_players_first_turn
from spirit.game.data_utils import SupporterCardDef


def _target(board, player_id) -> int:
    return 8 if second_players_first_turn(board, player_id) else 6


def _can_play(board, player_id, card=None) -> bool:
    """Not playable when the rest of the hand already holds the target
    (6, or 8 on the second player's first turn) or more: it would draw
    nothing (house ruling)."""
    hand = board.find_player_area(player_id, "hand")
    others = [c for c in (hand.children if hand else []) if c is not card]
    if card is None and others:
        others = others[1:]  # no specific copy given: leave one out
    return len(others) < _target(board, player_id)


async def lillie(ctx):
    await ctx.draw_until(_target(ctx.board, ctx.player_id))


card = SupporterCardDef(
    guid="43f67cc6-3536-5876-8894-846f904aa4b5",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lillie.Name",
    display_name="Lillie",
    searchable_by=["Lillie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=122,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    condition=_can_play,
    effect=lillie,
)
