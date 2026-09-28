"""Grimsley's Move (ME - Phantasmal Flames 90 -- JP M2 076/080).

Supporter.

  "Look at the top 7 cards of your deck and put a [D] Pokemon you find there
   onto your Bench. Shuffle the other cards and put them on the bottom of
   your deck. You can't use this card during your first turn."
"""

import random

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import is_basic_pokemon, is_pokemon_of_type
from spirit.game.session.passives import effective_bench_capacity


def _not_first_turn(board, player_id, card=None) -> bool:
    turn_state = getattr(board, "turn_state", None)
    return turn_state is not None and turn_state.turn_number > 2


async def grimsleys_move(ctx):
    top = ctx.deck_top(7)
    if not top:
        return
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    space = effective_bench_capacity(ctx.board, ctx.player_id) - (len(bench.children) if bench else 0)
    pool = [c for c in top if is_basic_pokemon(c) and is_pokemon_of_type(c, PokemonTypes.DARKNESS)]
    picks = []
    if pool and space > 0:
        picks = await ctx.choose_cards(pool, 1, minimum=0, display_cards=top,
                                       prompt="Choose a [D] Pokémon to put onto your Bench.")
    for pick in picks:
        await ctx.bench_pokemon(pick)
    rest = [c for c in top if c not in picks]
    random.shuffle(rest)
    for card in rest:
        await ctx.put_on_bottom_of_deck(card)


card = SupporterCardDef(
    guid="e5ed0edd-adcb-5150-b640-b32f22494ca4",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GrimsleysMove.Name",
    display_name="Grimsley's Move",
    searchable_by=["Grimsley's Move", "Supporter", "GrimsleysMove"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=_not_first_turn,
    effect=grimsleys_move,
)
