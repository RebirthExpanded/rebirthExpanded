"""Lickitung (SV05 124 -- JP SV5M 053; English TEF/124, TEF/180). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def tongue_pull(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    space = effective_bench_capacity(ctx.board, ctx.opponent_id) - len(ctx.opponent_bench())
    pool = [c for c in hand if is_basic_pokemon(c)]
    if not pool or space <= 0:
        return
    picks = await ctx.choose_cards(pool, min(2, space, len(pool)), minimum=0,
                                   prompt="Put up to 2 Basic Pokémon onto your opponent's Bench")
    for card in picks:
        await ctx.bench_pokemon(card)


card = PokemonCardDef(
    guid="a11f5a61-ea84-573f-b5a9-b7095b47b545",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    display_name="Lickitung",
    searchable_by=["Lickitung", "Basic"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=108,
    abilities=[
        Attack(
            title="Tongue Pull",
            game_text="Your opponent reveals their hand. Put up to 2 Basic Pokémon you find there onto your opponent's Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=tongue_pull,
        ),
        Attack(
            title="Strength",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
