"""Samurott (RSV10PT5 23 -- JP SV11W 020; English WHT/107, WHT/23). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su


def _has_bench(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return bool(bench and bench.children)


async def torrential_whirlpool(ctx):
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with your Active Pokémon")
    if target is None or not await ctx.switch_active(ctx.player_id, target):
        return
    await su.opponent_switches(ctx)


card = PokemonCardDef(
    guid="cd9b0fd7-c900-5306-b638-eeeb37088d66",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Samurott.Name",
    display_name="Samurott",
    searchable_by=["Samurott", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    family_id=501,
    abilities=[
        Ability(
            title="Torrential Whirlpool",
            game_text="Once during your turn, you may switch your Active Pokémon with 1 of your Benched Pokémon. If you do, switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            activation=Activations.ONCE_PER_TURN,
            condition=_has_bench,
            effect=torrential_whirlpool,
        ),
        Attack(
            title="Energized Slash",
            game_text="This attack does 50 more damage for each Energy attached to this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self"), 50, base=30),
        ),
    ],
)
