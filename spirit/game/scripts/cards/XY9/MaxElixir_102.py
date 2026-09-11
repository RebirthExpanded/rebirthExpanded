"""Max Elixir (XY - BREAKpoint 102/122 -- JP XY9-B 072/080).

Item.

  "Look at the top 6 cards of your deck and attach a basic Energy card you
   find there to a Basic Pokemon on your Bench. Shuffle the other cards
   back into your deck."

Playable only with a Basic on the Bench and a deck to look at; finding no
basic Energy still shows the 6 and shuffles.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import (is_basic_energy,
                                         is_basic_pokemon_in_play)


def _max_elixir_condition(board, player_id, pokemon=None) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return requires_deck(1)(board, player_id) and any(
        is_basic_pokemon_in_play(p) for p in (bench.children if bench else []))


async def max_elixir(ctx):
    top = ctx.deck_top(6)
    if not top:
        return
    energies = [c for c in top if is_basic_energy(c)]
    picks = await ctx.choose_cards(
        energies, 1, minimum=1 if energies else 0,
        prompt="Choose a basic Energy card to attach to a Benched Basic Pokémon.",
        display_cards=top if len(energies) < len(top) else None)
    if picks:
        targets = [p for p in ctx.my_bench() if is_basic_pokemon_in_play(p)]
        target = await ctx.choose_pokemon(targets, "Choose a Benched Basic Pokémon")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="c3c6300a-def0-5c57-b198-0de6a7710e8b",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxElixir.Name",
    display_name="Max Elixir",
    searchable_by=["Max Elixir", "Item", "MaxElixir"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    condition=_max_elixir_condition,
    effect=max_elixir,
)
