"""Decidueye ex (SV3 15 -- JP SVD 008; English OBF/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _freedom_condition(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return bool(bench and bench.children)


async def total_freedom(ctx):
    me = ctx.source
    if ctx.board.active_pokemon(ctx.player_id) is me:
        bench = ctx.my_bench()
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with") if bench else None
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    else:
        await ctx.switch_active(ctx.player_id, me)


card = PokemonCardDef(
    guid="3700ebb5-1134-583c-ac00-5319b5a2011e",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Decidueyeex.Name",
    display_name="Decidueye ex",
    searchable_by=["Decidueye ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=15,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Ability(
            title="Total Freedom",
            game_text="Once during your turn, you may use this Ability. If this Pokémon is on the Bench, switch it with your Active Pokémon. Or, if this Pokémon is in the Active Spot, switch it with 1 of your Benched Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_freedom_condition,
            effect=total_freedom,
        ),
        Attack(
            title="Hunting Arrow",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ac.snipe_attack(30, pool="bench", also_base=True),
        ),
    ],
)
