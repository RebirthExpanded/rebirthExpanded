"""Drowzee (SV1 82 -- JP SV1V 038; English SVI/210, SVI/82). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import support_common as su


async def forced_sleep(ctx):
    d = ctx.opponent_active()
    if d is None or ctx.effects_blocked(d):
        return
    new = await su.opponent_switches(ctx)
    if new is not None:
        await ctx.apply_special_condition(new, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="47c309dd-fbed-555f-9ae9-33e16e44a8df",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    display_name="Drowzee",
    searchable_by=["Drowzee", "Basic"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=96,
    abilities=[
        Attack(
            title="Forced Sleep",
            game_text="Your opponent chooses 1 of their Benched Pokémon and switches it with their Active Pokémon. The new Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=forced_sleep,
        ),
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
