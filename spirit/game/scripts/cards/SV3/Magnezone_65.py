"""Magnezone (SV3 65 -- JP SVD 038; English OBF/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


async def magnetic_repulsion(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is None or d in ctx.knockouts or ctx.effects_blocked(d) or not ctx.opponent_bench():
        return
    if await ctx.ask_yes_no("Switch out your opponent's Active Pokémon to the Bench?"):
        await su.opponent_switches(ctx)


card = PokemonCardDef(
    guid="cf3650b9-482e-5c9a-ac54-23acdcee8b5e",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=65,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Magnetic Repulsion",
            game_text="You may switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            effect=magnetic_repulsion,
        ),
        Attack(
            title="Thunder",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=ac.recoil_attack(30),
        ),
    ],
)
