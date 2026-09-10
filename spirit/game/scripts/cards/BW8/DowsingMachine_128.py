"""Dowsing Machine (BW - Plasma Storm 128/135).

Item, ACE SPEC.

  "Discard 2 cards from your hand. (If you can't discard 2 cards, you can't
   play this card.) Put a Trainer card from your discard pile into your
   hand."

Computer Search's sibling and the same two-card cost, but it fishes out of
the discard pile instead of the deck, and only Trainers. Both halves have
to be possible for it to be played: hand_size_at_least(3) is the printed
parenthesis, and a Trainer has to be sitting in the discard.

The Dowsing Machine being played is not among the candidates -- it only
reaches the discard after the effect resolves -- so the filter drops
ctx.source defensively.

The ACE SPEC deck limit is enforced in game/rules.py.
"""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.card_effects.trainers import hand_size_at_least
from spirit.game.session.effects import is_trainer_card


def _dowsing_playable(board, player_id, card=None):
    return (hand_size_at_least(3)(board, player_id)
            and requires_discard(is_trainer_card, 1)(board, player_id))


async def dowsing_machine(ctx):
    """Pay 2 from hand, then take a Trainer back out of the discard."""
    if len(await ctx.discard_from_hand(
            2, prompt="Discard 2 cards for Dowsing Machine")) < 2:
        return
    trainers = [c for c in ctx.discard_pile()
                if is_trainer_card(c) and c is not ctx.source]
    if not trainers:
        return
    picks = await ctx.choose_cards(
        trainers, 1, minimum=1,
        prompt="Choose a Trainer card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = ItemCardDef(
    guid="207c2818-c85b-5ae8-8135-b4b3f17d2147",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DowsingMachine.Name",
    display_name="Dowsing Machine",
    searchable_by=["Dowsing Machine", "Item", "ACE SPEC", "DowsingMachine"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=128,
    set_code="BW8",
    rarity=Rarities.Ace,
    effect=dowsing_machine,
    condition=_dowsing_playable,
)
