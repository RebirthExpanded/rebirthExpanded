"""Klawf (SV4 105 -- JP SV3a 031; English PAR/105). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _afflicted_self(ctx) -> bool:
    return bool(ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def boiled_press(ctx):
    await ctx.deal_damage()
    if ctx.attacker not in ctx.knockouts:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="cb11244b-00be-5433-87d6-ef675581c283",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klawf.Name",
    display_name="Klawf",
    searchable_by=["Klawf", "Basic"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=950,
    abilities=[
        Attack(
            title="Unhinged Scissors",
            game_text="If this Pokémon is affected by a Special Condition, this attack does 160 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_afflicted_self, 160),
        ),
        Attack(
            title="Boiled Press",
            game_text="This Pokémon is now Burned.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            effect=boiled_press,
        ),
    ],
)
