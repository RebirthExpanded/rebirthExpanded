"""Milotic (SV4 36 -- JP SV4M 014; English PAR/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def _bench_one_from_discard(ctx, pid):
    if effective_bench_capacity(ctx.board, pid) - len(ctx.board.find_player_area(pid, "bench").children) <= 0:
        return
    pool = [c for c in ctx.discard_pile(pid) if is_basic_pokemon(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Pokémon to put onto your Bench", player_id=pid)
        if picks:
            await ctx.bench_pokemon(picks[0])


async def lifeboat(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if not await ctx.ask_yes_no("Use Lifeboat?"):
        return
    await _bench_one_from_discard(ctx, ctx.opponent_id)
    await _bench_one_from_discard(ctx, ctx.player_id)


card = PokemonCardDef(
    guid="aa626088-69f3-5c77-8668-6856d8937650",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Lifeboat",
            game_text="Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Each player puts a Basic Pokémon from their discard pile onto their Bench. (Your opponent puts a Basic Pokémon onto their Bench first.)",
            trigger=Triggers.ON_EVOLVE,
            effect=lifeboat,
        ),
        Attack(
            title="Hypno Splash",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
