from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers, def_for
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def inviting_wink(ctx):
    """Evolved from hand: the opponent reveals their hand and any number of
    its Basic Pokemon go onto their Bench (Gloom's Poison Pollen shape)."""
    if not getattr(ctx, "evolved_from_hand", True):
        return
    opp = ctx.opponent_id
    bench = ctx.board.find_player_area(opp, "bench")
    space = effective_bench_capacity(ctx.board, opp) - (len(bench.children) if bench else 0)
    if space <= 0 or not ctx.hand(opp):
        return
    if not await ctx.ask_yes_no("Have your opponent reveal their hand?"):
        return
    hand = await ctx.reveal_hand(opp)
    basics = [c for c in hand if is_basic_pokemon(c)]
    if not basics:
        return
    picks = await ctx.choose_cards(
        basics, min(space, len(basics)), minimum=0,
        prompt="Choose any number of Basic Pokémon to put onto your opponent's Bench.")
    for pick in picks:
        await ctx.bench_pokemon(pick)

card = PokemonCardDef(
    guid="e7fd5b3c-fcb4-50c3-b58d-7bafa229bb33",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesRibombee.Name",
    display_name="Lillie's Ribombee",
    searchable_by=["Lillie's Ribombee", "Stage 1", "LilliesRibombee"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesCutiefly.Name",
    family_id=742,
    abilities=[
        Ability(
            title="Inviting Wink",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may have your opponent reveal their hand and you put any number of Basic Pok\u00e9mon you find there onto their Bench.",
            trigger=Triggers.ON_EVOLVE,
            effect=inviting_wink,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
        ),
    ],
)
