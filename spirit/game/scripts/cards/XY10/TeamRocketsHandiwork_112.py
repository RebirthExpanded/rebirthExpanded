"""Team Rocket's Handiwork (XY - Fates Collide 112/124).

Supporter.

  "Flip 2 coins. For each heads, discard 2 cards from the top of your
   opponent's deck."

Two coins, up to 4 cards off the top of THEIR deck. Both tails and the
card did nothing, which is the risk it is printed with -- the coins are the
effect, so it stays playable as long as they have a deck to mill.

The pool's first Fates Collide card, so XY10 joins the Expanded set list
(it was already in sets.json).
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


def _opponent_has_deck(board, player_id, card=None):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    deck = board.find_player_area(opponent, "deck")
    return bool(deck and deck.children)


async def team_rockets_handiwork(ctx):
    """Two coins; 2 off the top of their deck for each heads."""
    results = await ctx.flip_coins(2, "Team Rocket's Handiwork")
    heads = sum(1 for r in results if r)
    if heads <= 0:
        return
    await ctx.discard_cards(ctx.deck_top(heads * 2, player_id=ctx.opponent_id))


card = SupporterCardDef(
    guid="eaf6bcad-0fc8-5cbb-8a22-6648b136a99f",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsHandiwork.Name",
    display_name="Team Rocket's Handiwork",
    searchable_by=["Team Rocket's Handiwork", "Supporter", "TeamRocketsHandiwork"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=team_rockets_handiwork,
    condition=_opponent_has_deck,
)
