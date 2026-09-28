"""Naveen (ME - Perfect Order 79 -- JP M3 074).

Supporter.

  "Draw cards until you have 5 cards in your hand. Before drawing cards, you
   may discard any number of cards from your hand. (If you can't draw any
   cards in this way, you can't use this card.)"

Playable while the deck has a card: the optional discard can always bring
the hand under 5.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef


def _can_draw(board, player_id, card=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def naveen(ctx):
    hand = list(ctx.hand())
    if hand:
        picks = await ctx.choose_cards(hand, len(hand), minimum=0,
                                       prompt="Discard any number of cards from your hand (or none)")
        if picks:
            await ctx.discard_cards(picks)
    await ctx.draw_until(5)


card = SupporterCardDef(
    guid="1554f2d4-b877-5f56-9651-48cfb6027934",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Naveen.Name",
    display_name="Naveen",
    searchable_by=["Naveen", "Supporter", "Naveen"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    condition=_can_draw,
    effect=naveen,
)
