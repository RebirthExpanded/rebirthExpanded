"""Lapras ex (ME3 22 -- JP MP 002; English POR/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


async def hydro_turn(ctx):
    n = ac.count_energy("self", _PT.WATER)(ctx)
    if n:
        await ctx.deal_damage(30 * n)
    bench = ctx.my_bench()
    if bench and ctx.attacker not in ctx.knockouts:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="89b3d3b3-0237-5ed6-8580-581ac0987244",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Laprasex.Name",
    display_name="Lapras ex",
    searchable_by=["Lapras ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=22,
    set_code="ME3",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Hydro Turn",
            game_text="This attack does 30 damage for each Water Energy attached to this Pokémon. Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=hydro_turn,
        ),
        Attack(
            title="Surf",
            game_text="",
            cost={PokemonTypes.WATER: 3},
            damage=140,
        ),
    ],
)
