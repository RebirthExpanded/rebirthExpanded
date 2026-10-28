"""Shauntal (SV4 174 -- JP SV3a 059; English PAR/174, PAR/243). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def shauntal(ctx):
    results = await ctx.flip_coins(1, "Shauntal")
    if results and results[0]:
        bench = ctx.opponent_bench()
        if bench:
            target = await ctx.choose_pokemon(bench, "Choose the opponent's new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
    else:
        bench = ctx.my_bench()
        if bench:
            target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)


card = SupporterCardDef(
    guid="bfe7de60-2b5b-58b6-be54-cfefd0240ea2",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauntal.Name",
    display_name="Shauntal",
    searchable_by=["Shauntal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=174,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=shauntal,
)
