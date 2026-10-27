"""Nidoqueen (ME6 43 -- JP M6 043; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


def _opp_bench(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    bench = board.find_player_area(other, "bench") if other else None
    return bool(bench and bench.children)


async def mothers_lure(ctx):
    results = await ctx.flip_coins(1, "Mother's Lure")
    if results and results[0]:
        await su.gust_attack(damage_before=0)(ctx)


card = PokemonCardDef(
    guid="f08bd7e8-cf24-5d44-ad50-3e72f7ea008b",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen",
    searchable_by=["Nidoqueen", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=43,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=29,
    abilities=[
        Ability(
            title="Mother's Lure",
            game_text="Once during your turn, you may use this Ability. Flip a coin. If heads, switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_opp_bench,
            effect=mothers_lure,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=_hit_then_lock,
        ),
    ],
)
