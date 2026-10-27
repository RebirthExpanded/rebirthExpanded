"""Sableye (ME6 46 -- JP M6 046; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def lure_out(ctx):
    opp = ctx.opponent_id
    top = ctx.deck_top(5, player_id=opp)
    if not top:
        return
    await ctx.reveal_cards(top)
    space = effective_bench_capacity(ctx.board, opp) - len(ctx.opponent_bench())
    pool = [c for c in top if is_basic_pokemon(c)]
    if pool and space > 0:
        picks = await ctx.choose_cards(pool, min(space, len(pool)), minimum=0, display_cards=top,
                                       prompt="Choose any number of Basic Pokémon to put onto your opponent's Bench.")
        for card in picks:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck(opp)


card = PokemonCardDef(
    guid="5efec8fa-eef9-5ece-8710-8121e4097deb",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=302,
    abilities=[
        Attack(
            title="Lure Out",
            game_text="Reveal the top 5 cards of your opponent's deck, put any number of Basic Pokémon you find there onto their Bench, and shuffle the other cards back into their deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=lure_out,
        ),
        Attack(
            title="Ominous Lick",
            game_text="Put 5 damage counters on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=ac.place_counters(5, "choose_any_opponent"),
        ),
    ],
)
