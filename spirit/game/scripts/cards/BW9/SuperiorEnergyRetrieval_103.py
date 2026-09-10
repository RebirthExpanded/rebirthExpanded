"""Superior Energy Retrieval (BW - Plasma Freeze 103/116 --
JP BW8 047/051).

Item.

  "You can't use this card unless you discard 2 cards from your hand.

   Put 4 basic Energy cards from your discard pile into your hand."

Energy Retrieval's big brother, and the cost is a real one: the two cards
leave your hand before the four come back, so it is a 3-for-4 that only
pays off with the Energy already down there.

The one subtlety is the printed order. The Japanese text spells out that
Energy discarded BY THIS CARD cannot be chosen, so the candidate list is
taken before the cost is paid -- pitching two basic Energy to it does not
put them back in reach.

Playability asks for both halves: 3 cards in hand (the two paid plus this
one) and a basic Energy in the discard.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.card_effects.trainers import hand_size_at_least
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_basic_energy

TAKE = 4


def _superior_retrieval_playable(board, player_id, card=None):
    return (hand_size_at_least(3)(board, player_id)
            and requires_discard(is_basic_energy, 1)(board, player_id))


async def superior_energy_retrieval(ctx):
    """Pay 2 from hand, then take up to 4 basic Energy back."""
    # Read the pile BEFORE paying: "you can't choose Energy discarded by
    # this card's effect".
    available = [c for c in ctx.discard_pile() if is_basic_energy(c)]
    if len(await ctx.discard_from_hand(
            2, prompt="Discard 2 cards for Superior Energy Retrieval")) < 2:
        return
    if not available:
        return
    picks = await ctx.choose_cards(
        available, min(TAKE, len(available)), minimum=min(TAKE, len(available)),
        prompt="Choose basic Energy cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = ItemCardDef(
    guid="324a4a72-a6b2-565d-93dc-59caa9411197",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperiorEnergyRetrieval.Name",
    display_name="Superior Energy Retrieval",
    searchable_by=["Superior Energy Retrieval", "Item",
                   "SuperiorEnergyRetrieval"],
    subtypes=["Item"],
    collector_number=103,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    effect=superior_energy_retrieval,
    condition=_superior_retrieval_playable,
)
