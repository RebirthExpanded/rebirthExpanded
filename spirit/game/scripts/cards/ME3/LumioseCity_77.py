"""Lumiose City (ME - Perfect Order 77 -- JP M3 077).

Stadium.

  "Once during each player's turn, that player may search their deck for a
   Basic Pokemon and put it onto their Bench. Then, that player shuffles
   their deck. If a player searches their deck in this way, their turn
   ends."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, Activations, StadiumCardDef
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


def _lumiose_condition(board, player_id, stadium=None) -> bool:
    bench = board.find_player_area(player_id, "bench")
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and bench is not None and \
        len(bench.children) < effective_bench_capacity(board, player_id)


async def lumiose_city(ctx):
    picks = await ctx.search_deck(is_basic_pokemon, count=1, minimum=0,
                                  prompt="Choose a Basic Pokémon to put onto your Bench.")
    for pick in picks:
        await ctx.bench_pokemon(pick)
    await ctx.shuffle_deck()
    ctx.ends_turn = True


card = StadiumCardDef(
    guid="2c4aba6d-f947-54a6-8270-9f7ad4912268",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LumioseCity.Name",
    display_name="Lumiose City",
    searchable_by=["Lumiose City", "Stadium", "LumioseCity"],
    subtypes=["Stadium"],
    collector_number=77,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Lumiose City",
        game_text="Once during each player's turn, that player may search their deck for a Basic Pokémon and put it onto their Bench. Then, that player shuffles their deck. If a player searches their deck in this way, their turn ends.",
        activation=Activations.ONCE_PER_TURN,
        condition=_lumiose_condition,
        effect=lumiose_city,
    ),
)
