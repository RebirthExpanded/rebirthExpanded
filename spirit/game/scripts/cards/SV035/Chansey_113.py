"""Chansey (SV035 113 -- JP SV2a 113; English MEW/113). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import effective_bench_capacity, putting_into_play_blocked


async def lucky_bonus(ctx):
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    if bench is None or len(bench.children) >= effective_bench_capacity(ctx.board, ctx.player_id):
        return
    if putting_into_play_blocked(ctx.board, ctx.player_id, ctx.source):
        return
    if not await ctx.ask_yes_no("Put this Pokémon onto your Bench?"):
        return
    if not await ctx.bench_pokemon(ctx.source):
        return
    results = await ctx.flip_coins(1, "Lucky Bonus")
    if results and results[0]:
        await ctx.take_prizes(1)


card = PokemonCardDef(
    guid="71b1a6ed-ef0b-56c4-a71f-742cea2fad20",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=440,
    abilities=[
        Ability(
            title="Lucky Bonus",
            game_text="If you took this Pokémon as a face-down Prize card during your turn and your Bench isn't full, before you put it into your hand, you may put it onto your Bench. If you put this Pokémon onto your Bench in this way, flip a coin. If heads, take 1 more Prize card.",
            trigger=Triggers.ON_TAKEN_AS_PRIZE,
            effect=lucky_bonus,
        ),
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
