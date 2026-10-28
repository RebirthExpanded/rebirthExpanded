"""Bramblin (SV2 22 -- JP SV2P 010; English PAL/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def ride_the_wind(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Ride the Wind")
    bench = ctx.my_bench()
    if results and results[0] and bench and ctx.attacker not in ctx.knockouts:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="e1a1e524-2f0e-50a0-83e0-cc4dd5f3f4f2",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name",
    display_name="Bramblin",
    searchable_by=["Bramblin", "Basic"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=946,
    abilities=[
        Attack(
            title="Ride the Wind",
            game_text="Flip a coin. If heads, switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=ride_the_wind,
        ),
    ],
)
