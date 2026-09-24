"""Redeemable Ticket (SV - Journey Together 156/159 -- JP SV9 090/100).

Item.

  "Count your Prize cards, shuffle them, and put them on the bottom of your
   deck. Then, put that many cards from the top of your deck face down as
   your Prize cards."

A re-deal of your own spread: the same NUMBER of Prizes comes back, drawn
from the top of a deck the old Prizes are now sitting under. It is the
answer to a prized key card -- and, being a re-deal rather than a shuffle
into the deck, the cards that go under are the last ones you will see.

Two accounting points:

The Prizes you have already TAKEN must survive this. prizes_taken is
prizes_dealt minus the pile, and deal_from_deck adds to prizes_dealt, so
handing back the same count would otherwise reset the total to zero and
lie to every card that reads it (Ace Trainer, Beauty-GX, Counter Energy).
The dealt count is restored afterwards, which is right because the pile
size does not change.

The "then" clause needs no gate: whatever went to the bottom of the deck
is in the deck, so the deck always holds at least that many cards to lay
back out. The card does need Prizes to count, which is only false once
the game is already over, but the condition says so anyway.
"""

import random

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import prizes_remaining
from spirit.game.data_utils import ItemCardDef


def _redeemable_ticket_playable(board, player_id, card=None):
    return prizes_remaining(board, player_id) > 0


async def redeemable_ticket(ctx):
    """Shuffle your Prizes to the bottom of the deck and lay out that many."""
    board = ctx.board
    pid = ctx.player_id
    area = board.find_player_area(pid, "prizePile")
    if area is None or not area.children:
        return
    prizes = list(area.children)
    random.shuffle(prizes)
    dealt_before = board.prizes_dealt.get(pid, 0)
    for prize in prizes:
        await ctx.put_on_bottom_of_deck(prize)
    dealt = board.deal_from_deck(pid, "prizePile", len(prizes))
    for entry in dealt:
        ctx._queue(ctx.session._entity_moved_msg(
            entry["entity_id"], entry["destination_id"], entry["position"]))
        # Re-hide it: a card the client has already seen (a deck search
        # introduces the whole deck) would otherwise land face up.
        ctx._queue(ctx.session._attributes_reset_msg(entry["entity_id"]))
    # Same count out, same count in: the Prizes already taken are unchanged.
    board.prizes_dealt[pid] = dealt_before
    ctx._queue(ctx.session._refresh_prize_gaps(pid, area))


card = ItemCardDef(
    guid="f06e66d7-8277-55d6-a446-3d06bb749771",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedeemableTicket.Name",
    display_name="Redeemable Ticket",
    searchable_by=["Redeemable Ticket", "Item", "RedeemableTicket"],
    subtypes=["Item"],
    collector_number=156,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=redeemable_ticket,
    condition=_redeemable_ticket_playable,
)
