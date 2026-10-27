"""Mandibuzz (RSV10PT5 64 -- JP SV11B 064; English WHT/145, WHT/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


def _look_for_prey_condition(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    hand = board.find_player_area(other, "hand") if other else None
    bench = board.find_player_area(other, "bench") if other else None
    return bool(hand and hand.children) and len(bench.children if bench else []) < effective_bench_capacity(board, other)


def _prey(card) -> bool:
    return is_basic_pokemon(card) and (card.get_attribute(AttrID.HP, 0) or 0) <= 70


async def look_for_prey(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    pool = [c for c in hand if _prey(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Pokémon to put onto your opponent's Bench")
    if picks:
        await ctx.bench_pokemon(picks[0])


card = PokemonCardDef(
    guid="2567277f-fcdd-536b-8188-9551cbc8ab7e",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name",
    display_name="Mandibuzz",
    searchable_by=["Mandibuzz", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    family_id=629,
    abilities=[
        Ability(
            title="Look for Prey",
            game_text="Once during your turn, you may use this Ability. Your opponent reveals their hand, and you put a Basic Pokémon with 70 HP or less that you find there onto your opponent's Bench.",
            activation=Activations.ONCE_PER_TURN,
            condition=_look_for_prey_condition,
            effect=look_for_prey,
        ),
        Attack(
            title="Cutting Wind",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)
