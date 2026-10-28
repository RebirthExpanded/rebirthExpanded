"""Quaquaval ex (SVP 35 -- JP SV1a 030; English PAL/235, PAL/260, PAL/273, PAL/52, SVP/35, SVP/84). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def exciting_dance(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench or ctx.attacker in ctx.knockouts:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
    if target is not None and await ctx.switch_active(ctx.player_id, target):
        await su.opponent_switches(ctx)


async def spiral_shot(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    n = min(2, len(pool))
    if n and ctx.attacker not in ctx.knockouts:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Energy to put into your hand")
        await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="ad8bda61-3530-5d1c-bb22-3ea18a778829",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaquavalex.Name",
    display_name="Quaquaval ex",
    searchable_by=["Quaquaval ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=35,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name",
    family_id=912,
    abilities=[
        Attack(
            title="Exciting Dance",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. If you do, switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            effect=exciting_dance,
        ),
        Attack(
            title="Spiral Shot",
            game_text="Put 2 Energy attached to this Pokémon into your hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=spiral_shot,
        ),
    ],
)
