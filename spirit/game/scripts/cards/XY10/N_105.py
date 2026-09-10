"""N (XY - Fates Collide 105/124).

Supporter.

  "Each player shuffles his or her hand into his or her deck. Then, each
   player draws a card for each of his or her remaining Prize cards."

Iono's ancestor, and the difference is where the hand goes: N shuffles it
INTO the deck, so the shuffle itself is something that can be done with an
empty hand -- what N needs is a deck. One deck between the two players is
enough, since each half runs on its own player's, so the gate is
requires_any_deck.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_any_deck


def _prizes_left(ctx, pid):
    area = ctx.board.find_player_area(pid, "prizePile")
    return len(area.children) if area else 0


async def n_effect(ctx):
    """Both hands go back, then each player draws their Prize count."""
    for pid in (ctx.player_id, ctx.opponent_id):
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
    for pid in (ctx.player_id, ctx.opponent_id):
        await ctx.draw_cards(_prizes_left(ctx, pid), pid)


card = SupporterCardDef(
    guid="cd41d889-fa16-550f-a310-286a7969bf24",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N", "Supporter"],
    subtypes=["Supporter"],
    collector_number=105,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=n_effect,
    condition=requires_any_deck(),
)
