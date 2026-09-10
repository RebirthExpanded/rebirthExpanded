"""Ace Trainer (XY - Ancient Origins 69/98).

Supporter.

  "You can play this card only if you have more Prize cards left than your
   opponent."
  "Each player shuffles his or her hand into his or her deck. Then, draw 6
   cards. Your opponent draws 3 cards."

The Prize clause is printed, so it is half the condition; the other half
is N's, since the hands go INTO the decks and the shuffle is what keeps
the "Then" alive -- one deck between the two players is enough.

Behind on Prizes means you are losing, which is the whole point: 6 to
their 3.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import all_of, requires_any_deck


def _behind_on_prizes(board, player_id, card=None):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False

    def prizes(pid):
        area = board.find_player_area(pid, "prizePile")
        return len(area.children) if area else 0

    return prizes(player_id) > prizes(opponent)


async def ace_trainer(ctx):
    """Both hands go back; you draw 6, they draw 3."""
    for pid in (ctx.player_id, ctx.opponent_id):
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
    await ctx.draw_cards(6)
    await ctx.draw_cards(3, ctx.opponent_id)


card = SupporterCardDef(
    guid="f63fbc5f-a30f-5591-a45b-a66f33e15437",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AceTrainer.Name",
    display_name="Ace Trainer",
    searchable_by=["Ace Trainer", "Supporter", "AceTrainer"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    effect=ace_trainer,
    condition=all_of(_behind_on_prizes, requires_any_deck()),
)
