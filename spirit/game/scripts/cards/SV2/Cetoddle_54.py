"""Cetoddle (SV2 54 -- JP SV2P 021; English PAL/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def rest(ctx):
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    await ctx.heal(60, ctx.attacker)


card = PokemonCardDef(
    guid="f5c12ff9-6440-5365-95ac-1bc4ed168e2a",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    display_name="Cetoddle",
    searchable_by=["Cetoddle", "Basic"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=974,
    abilities=[
        Attack(
            title="Rest",
            game_text="This Pokémon is now Asleep. Heal 60 damage from it.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=rest,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.recoil_attack(10),
        ),
    ],
)
