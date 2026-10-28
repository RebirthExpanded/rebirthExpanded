"""Baltoy (SV3 94 -- JP SV3 049; English OBF/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def rapid_spin(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench or ctx.attacker in ctx.knockouts:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
    if target is not None and await ctx.switch_active(ctx.player_id, target):
        await su.opponent_switches(ctx)


card = PokemonCardDef(
    guid="da46ee73-3e97-5c68-94bf-c0faf929addc",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    display_name="Baltoy",
    searchable_by=["Baltoy", "Basic"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=343,
    abilities=[
        Attack(
            title="Rapid Spin",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. If you do, switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=rapid_spin,
        ),
    ],
)
