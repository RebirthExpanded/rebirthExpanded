"""Kyogre ex (SVP 178 -- JP SVM 037; English SVP/178). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


async def winding_waves(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is None or d in ctx.knockouts or ctx.effects_blocked(d) or not ctx.opponent_bench():
        return
    if await ctx.ask_yes_no("Switch out your opponent's Active Pokémon to the Bench?"):
        await su.opponent_switches(ctx)


card = PokemonCardDef(
    guid="2aa01fb2-4961-5bd6-8bec-a44d883e6c1b",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogreex.Name",
    display_name="Kyogre ex",
    searchable_by=["Kyogre ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=178,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Winding Waves",
            game_text="You may switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=winding_waves,
        ),
        Attack(
            title="Tidal Surge",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=230,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
