"""Palkia (ME6A 14 -- JP M6a 014; English 30C/20). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def wormhole(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is None or not await ctx.switch_active(ctx.player_id, target):
        return
    if ctx.opponent_bench():
        await su.opponent_switches(ctx)


card = PokemonCardDef(
    guid="a2017f8b-8290-55cf-a33d-d87bf56ea3fa",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name",
    display_name="Palkia",
    searchable_by=["Palkia", "Basic"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=484,
    abilities=[
        Attack(
            title="Wormhole",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. If you do, switch out your oppoennt's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=wormhole,
        ),
    ],
)
