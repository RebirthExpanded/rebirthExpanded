"""Munna (ZSV10PT5 35 -- JP SV11B 038; English BLK/116, BLK/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def rest(ctx):
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    await ctx.heal(30, ctx.attacker)


card = PokemonCardDef(
    guid="38af222b-1fb4-5931-84d1-58b4ab9bab2d",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    display_name="Munna",
    searchable_by=["Munna", "Basic"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=517,
    abilities=[
        Attack(
            title="Rest",
            game_text="This Pokémon is now Asleep. Heal 30 damage from it.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=rest,
        ),
        Attack(
            title="Mumble",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
