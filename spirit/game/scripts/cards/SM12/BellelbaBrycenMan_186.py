"""Bellelba & Brycen-Man (SM - Cosmic Eclipse 186/236).

Supporter, TAG TEAM.

  "Discard 3 cards from the top of each player's deck."
  "When you play this card, you may discard 3 other cards from your hand.
   If you do, each player discards their Benched Pokemon until they have 3
   Benched Pokemon. Your opponent discards first."

Guzma & Hala's shape again -- a free half plus a paid half -- with a
harsher pair of halves. The mill hits BOTH decks and is unconditional;
the 3-card discard buys the Bench squeeze.

"Your opponent discards first" is printed, and it matters: what they put
into the discard is on the table before you choose your own, so the loop
runs opponent then self rather than the engine's usual active-player-first
order. That is the one thing this card does that the bench-shrink ruling
does not, so it borrows the ruling's pieces (prompt_entity_picker plus
_discard_bench_stack) rather than enforce_bench_capacity itself, which
shrinks to the CAPACITY rather than to a number the card names.

Discarding a Benched Pokemon this way is not a Knock Out -- no prizes and
no ON_KNOCKED_OUT -- which is what _discard_bench_stack already means.

The choreography is flushed before each picker so the mill, and then the
opponent's discards, are visibly done before the next player is asked.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.models.board import PokemonEntity
from spirit.game.session.constants import PROMPT_DISCARD_BENCH

MILL_PER_PLAYER = 3
BENCH_LIMIT = 3
HAND_COST = 3


async def _shrink_bench_to(ctx, player_id: str, limit: int) -> None:
    """That player discards Benched Pokemon of their choice down to `limit`."""
    session, board = ctx.session, ctx.board
    bench = board.find_player_area(player_id, "bench")
    if bench is None:
        return
    candidates = [c for c in bench.children if isinstance(c, PokemonEntity)]
    overflow = len(candidates) - limit
    if overflow <= 0:
        return
    await ctx.flush_choreography()
    picked_ids = await session.prompt_entity_picker(
        player_id, candidates[0].entity_id, candidates, overflow,
        minimum=overflow, prompt=PROMPT_DISCARD_BENCH,
    )
    for entity_id in picked_ids[:overflow]:
        picked = board.get_entity(entity_id)
        if isinstance(picked, PokemonEntity) and picked.parent is bench:
            await session._discard_bench_stack(player_id, picked)


async def bellelba_and_brycen_man(ctx):
    """Mill 3 off both decks; pay 3 from hand to squeeze both Benches to 3."""
    for player_id in (ctx.player_id, ctx.opponent_id):
        await ctx.discard_cards(ctx.deck_top(MILL_PER_PLAYER, player_id))

    if len(ctx.hand()) < HAND_COST:
        return
    if not await ctx.ask_yes_no(
            "Discard 3 cards to make each player discard down to "
            "3 Benched Pokémon?"):
        return
    paid = await ctx.discard_from_hand(
        HAND_COST, minimum=HAND_COST, prompt="Choose 3 cards to discard")
    if len(paid) < HAND_COST:
        return
    # Printed order: theirs first, so their choice is public before yours.
    for player_id in (ctx.opponent_id, ctx.player_id):
        await _shrink_bench_to(ctx, player_id, BENCH_LIMIT)


card = SupporterCardDef(
    guid="138ffcaa-5146-5450-8849-d9e4afb25a84",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BellelbaBrycenMan.Name",
    display_name="Bellelba & Brycen-Man",
    searchable_by=["Bellelba & Brycen-Man", "Supporter", "TAG TEAM",
                   "BellelbaBrycenMan"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=186,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=bellelba_and_brycen_man,
)
