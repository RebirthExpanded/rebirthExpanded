"""Duskull (XY - Flashfire 38/106 -- JP XY2 033/080).

Basic Psychic Pokemon. HP 50, weakness Darkness x2, resistance Fighting
-20, retreat 1.

  Revival  [C]  Put a Basic Pokemon from your opponent's discard pile onto
                their Bench.
  Sneaky Placement  [P]  Put 1 damage counter on your opponent's Active
                         Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def revival(ctx):
    opp = ctx.opponent_id
    bench = ctx.board.find_player_area(opp, "bench")
    if bench is None or len(bench.children) >= effective_bench_capacity(ctx.board, opp):
        return
    basics = [c for c in ctx.discard_pile(opp) if is_basic_pokemon(c)]
    if not basics:
        return
    picks = await ctx.choose_cards(basics, 1, minimum=1,
                                   prompt="Choose a Basic Pokémon to put onto your opponent's Bench")
    if picks:
        await ctx.bench_pokemon(picks[0])


card = PokemonCardDef(
    guid="bf45e474-406a-5d6a-b467-9a4f4ed7ffd9",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    display_name="Duskull",
    searchable_by=["Duskull", "Basic"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=355,
    abilities=[
        Attack(title="Revival",
               game_text="Put a Basic Pokémon from your opponent's discard pile onto their Bench.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0, effect=revival),
        Attack(title="Sneaky Placement",
               game_text="Put 1 damage counter on your opponent's Active Pokémon.",
               cost={PokemonTypes.PSYCHIC: 1}, damage=0, effect=place_counters(1)),
    ],
)
