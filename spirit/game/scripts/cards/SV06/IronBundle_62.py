"""Iron Bundle (SV06 62 -- JP SV6 037; English TWM/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def interjet(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench or ctx.attacker in ctx.knockouts:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
    if target is not None and await ctx.switch_active(ctx.player_id, target):
        await su.opponent_switches(ctx)


card = PokemonCardDef(
    guid="926f4ffe-a16c-59bd-b959-9444b517c9f8",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBundle.Name",
    display_name="Iron Bundle",
    searchable_by=["Iron Bundle", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=62,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=991,
    abilities=[
        Attack(
            title="Interjet",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. If you do, switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=interjet,
        ),
    ],
)
