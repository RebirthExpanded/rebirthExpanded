"""Chimecho (SV045 30 -- JP SV4M 028; English PAF/30). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def sleep_inducer(ctx):
    old = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if old is None or not bench or ctx.effects_blocked(old):
        return
    target = await ctx.choose_pokemon(bench, "Choose the opponent's new Active Pokémon")
    if target is not None and await ctx.switch_active(ctx.opponent_id, target):
        await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="24065b14-f67b-526e-9f7d-18bf572e0d94",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho",
    searchable_by=["Chimecho", "Basic"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=433,
    abilities=[
        Attack(
            title="Sleep Inducer",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot. The new Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=sleep_inducer,
        ),
        Attack(
            title="Psyshot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
