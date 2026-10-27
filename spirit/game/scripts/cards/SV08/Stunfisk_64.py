"""Stunfisk (SV08 64 -- JP SV8 040; English SSP/202, SSP/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def paralyzing_crackle(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Paralyzing Crackle")
    d = ctx.opponent_active()
    if not (results and results[0]) or d is None or d in ctx.knockouts:
        return
    await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)
    if ctx.attached_energies(d) and not ctx.effects_blocked(d):
        await ctx.discard_energy_from(d, 1, minimum=1, prompt="Choose an Energy to discard")


card = PokemonCardDef(
    guid="4375cdaf-6e4c-55a5-854f-9d8e9531c2d6",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name",
    display_name="Stunfisk",
    searchable_by=["Stunfisk", "Basic"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=618,
    abilities=[
        Attack(
            title="Paralyzing Crackle",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed, and discard an Energy from that Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=paralyzing_crackle,
        ),
    ],
)
