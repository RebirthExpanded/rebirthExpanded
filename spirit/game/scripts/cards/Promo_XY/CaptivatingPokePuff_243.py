"""Captivating Poke Puff (JP XY-P 243, Pokemon Card Gym promo).

Item.

  "Look at your opponent's hand, choose as many Basic Pokemon as you like
   from it, and put them onto their Bench."

A Japan-only promo, so the Japanese promo number stands; the English
name is the card's own (Captivating Poke Puff).

It fills THEIR Bench, which is the whole point: a wider Bench is more to
snipe at, and the Basics it forces down are Basics they no longer hold for
a Marnie or an N. Their Bench capacity is the limit, so it stops once
there is no room, and effect-driven benching is what this is -- no on-play
trigger fires for the Pokemon it puts down.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


def _their_basics_in_hand(board, player_id):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if opponent is None:
        return []
    hand = board.find_player_area(opponent, "hand")
    return [c for c in (hand.children if hand else []) if is_basic_pokemon(c)]


def _captivating_poke_puff_playable(board, player_id, card=None):
    """Nothing to move, or nowhere to put it, and the card does nothing."""
    if not _their_basics_in_hand(board, player_id):
        return False
    opponent = next((p for p in board.player_ids if p != player_id), None)
    bench = board.find_player_area(opponent, "bench") if opponent else None
    if bench is None:
        return False
    return len(bench.children) < effective_bench_capacity(board, opponent)


async def captivating_poke_puff(ctx):
    """Their hand opens; every Basic you pick lands on their Bench."""
    candidates = _their_basics_in_hand(ctx.board, ctx.player_id)
    if not candidates:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    picks = await ctx.choose_cards(
        candidates, len(candidates), minimum=0,
        prompt="Choose Basic Pokémon to put onto your opponent's Bench.",
    )
    for pokemon in picks:
        if not await ctx.bench_pokemon(pokemon):
            break   # their Bench filled up


card = ItemCardDef(
    guid="01ef4c40-956f-516f-b76e-c34233eabf0b",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CaptivatingPokePuff.Name",
    display_name="Captivating Poké Puff",
    searchable_by=["Captivating Poké Puff", "Captivating Poke Puff",
                   "Item", "CaptivatingPokePuff"],
    subtypes=["Item"],
    collector_number=243,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=captivating_poke_puff,
    condition=_captivating_poke_puff_playable,
)
