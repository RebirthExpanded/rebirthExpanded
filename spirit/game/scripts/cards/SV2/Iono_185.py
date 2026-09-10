"""Iono (SV - Paldea Evolved 185/193).

Supporter.

  "Each player shuffles their hand and puts it on the bottom of their deck.
   If either player put any cards on the bottom of their deck in this way,
   each player draws a card for each of their remaining Prize cards."

Marnie's wording with the draw scaled to Prizes, and the same gate: the
hands go UNDER the decks with no deck shuffle, so with both hands empty
nothing goes down and the "If either player" clause never fires. One card
between the two hands is enough -- marnie_playable asks exactly that, this
Iono aside.

Where N shuffles hands INTO decks and so only needs a deck, Iono needs a
hand.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import marnie_playable


def _prizes_left(ctx, pid):
    area = ctx.board.find_player_area(pid, "prizePile")
    return len(area.children) if area else 0


async def iono(ctx):
    """Both hands go under the decks, then each draws their Prize count."""
    moved = 0
    for pid in (ctx.player_id, ctx.opponent_id):
        hand = ctx.hand(pid)
        moved += len(hand)
        for card in hand:
            await ctx.put_on_bottom_of_deck(card)
    if moved <= 0:
        return
    for pid in (ctx.player_id, ctx.opponent_id):
        await ctx.draw_cards(_prizes_left(ctx, pid), pid)


card = SupporterCardDef(
    guid="9f553bbf-41b2-5831-aa42-c4975a39894d",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iono.Name",
    display_name="Iono",
    searchable_by=["Iono", "Supporter"],
    subtypes=["Supporter"],
    collector_number=185,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=iono,
    condition=marnie_playable,
)
