"""Accompanying Flute (SV - Twilight Masquerade 142/167 -- JP SV6 091/101, the art here).

Item.

  "Reveal the top 5 cards of your opponent's deck. You may choose any
   number of Basic Pokemon you find there and put those Pokemon onto
   their Bench. Your opponent shuffles the other cards back into their
   deck."

The five are revealed to both players; the user picks among the Basics,
capped by the room on THEIR Bench; the put is an effect (no on-play
triggers), and the rest is shuffled back.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


def _condition(board, player_id, pokemon=None) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    deck = board.find_player_area(opponent, "deck") if opponent else None
    return bool(deck) and bool(deck.children)


async def accompanying_flute(ctx):
    top = ctx.deck_top(5, player_id=ctx.opponent_id)
    if not top:
        return
    await ctx.reveal_cards(top)
    basics = [c for c in top if is_basic_pokemon(c)]
    bench = ctx.board.find_player_area(ctx.opponent_id, "bench")
    room = effective_bench_capacity(ctx.board, ctx.opponent_id) - len(bench.children)
    if basics and room > 0:
        picks = await ctx.choose_cards(
            basics, min(len(basics), room), minimum=0,
            prompt="Choose any number of Basic Pokémon to put onto your opponent's Bench",
            display_cards=top if len(basics) < len(top) else None)
        for card in picks:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck(ctx.opponent_id)


card = ItemCardDef(
    guid="753cf644-1cbc-5198-b464-ca18ec802a76",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AccompanyingFlute.Name",
    display_name="Accompanying Flute",
    searchable_by=["Accompanying Flute", "Item", "AccompanyingFlute"],
    subtypes=["Item"],
    collector_number=142,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=_condition,
    effect=accompanying_flute,
)
