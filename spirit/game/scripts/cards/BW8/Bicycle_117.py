"""Bicycle (BW - Plasma Storm 117/135).

Item.

  "Draw cards until you have 4 cards in your hand."

Nothing to do with 4 or more already in hand (this Bicycle aside, since it
leaves the hand on the way), or with an empty deck -- so both are its
playability condition.

The pool's first Plasma Storm card, so BW8 joins the Expanded set list (it
was already in sets.json).
"""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect


def _bicycle_playable(board, player_id, card=None):
    """Room under 4 in hand, and a deck to draw from."""
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    if deck is None or not deck.children:
        return False
    held = [c for c in (hand.children if hand else []) if c is not card]
    return len(held) < 4


card = ItemCardDef(
    guid="be31bced-b179-5543-80dd-25b9735b1fbd",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bicycle.Name",
    display_name="Bicycle",
    searchable_by=["Bicycle", "Item"],
    subtypes=["Item"],
    collector_number=117,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=draw_until_effect(4),
    condition=_bicycle_playable,
)
