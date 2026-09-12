"""Hooligans Jim & Cas (BW - Dark Explorers 95/108 -- JP BW4-B 068/069, the art here).

Supporter.

  "Flip a coin. If heads, choose 3 random cards from your opponent's hand.
   Your opponent reveals those cards and shuffles them into his or her
   deck."

The three are drawn blind (random.sample), shown to both players, then
shuffled into their deck. Playable while the opponent holds a card.
"""

import random

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef


def _condition(board, player_id, pokemon=None) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    hand = board.find_player_area(opponent, "hand") if opponent else None
    return bool(hand) and bool(hand.children)


async def hooligans_jim_and_cas(ctx):
    heads = await ctx.flip_coins(1, "Hooligans Jim & Cas")
    if not (heads and heads[0]):
        return
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    picks = random.sample(hand, min(3, len(hand)))
    await ctx.reveal_cards(picks)
    await ctx.shuffle_into_deck(picks, ctx.opponent_id)


card = SupporterCardDef(
    guid="90224562-9142-5e61-a0d8-58c089037b88",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HooligansJimCas.Name",
    display_name="Hooligans Jim & Cas",
    searchable_by=["Hooligans Jim & Cas", "Supporter", "HooligansJimCas"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    condition=_condition,
    effect=hooligans_jim_and_cas,
)
