"""Slowpoke (SV1 42 -- JP SV1V 019; English PAF/116, SVI/204, SVI/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def rest(ctx):
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    await ctx.heal(30, ctx.attacker)


card = PokemonCardDef(
    guid="955cd070-ec59-5096-8474-fa28f89af52f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=79,
    abilities=[
        Attack(
            title="Rest",
            game_text="This Pokémon is now Asleep. Heal 30 damage from it.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=rest,
        ),
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
