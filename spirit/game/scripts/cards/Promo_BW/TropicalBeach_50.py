"""Tropical Beach (BW Black Star Promo BW50 -- JP BW-P, Worlds 2012).

Stadium.

  "Once during each player's turn, that player may draw cards until they
   have 7 cards in their hand. If they do, their turn ends."

Not offered with 7 or more already in hand or an empty deck (nothing would
be drawn, so the turn would not end either).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, Activations, StadiumCardDef


def _can_draw_toward_seven(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return len(hand.children if hand else []) < 7 \
        and bool(deck and deck.children)


async def tropical_beach(ctx):
    drew = await ctx.draw_until(7)
    if drew:
        ctx.ends_turn = True


ABILITY = Ability(
    title="Tropical Beach",
    game_text="Once during each player's turn, that player may draw cards until they have 7 cards in their hand. If they do, their turn ends.",
    activation=Activations.ONCE_PER_TURN,
    condition=_can_draw_toward_seven,
    effect=tropical_beach,
)

card = StadiumCardDef(
    guid="e3e4b255-b9e4-5555-acff-66aa72e58830",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalBeach.Name",
    display_name="Tropical Beach",
    searchable_by=["Tropical Beach", "Stadium", "TropicalBeach"],
    subtypes=["Stadium"],
    collector_number=50,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    ability=ABILITY,
)
