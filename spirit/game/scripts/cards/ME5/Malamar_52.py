"""Malamar (ME5 52 -- JP M5 050; English PBL/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.attributes import SpecialConditions


def _has_condition(pokemon, *conditions) -> bool:
    have = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [] if pokemon is not None else []
    return any(CLIENT_SPECIAL_CONDITION_NAMES[c] in have for c in conditions)


async def brain_crush(ctx):
    if _has_condition(ctx.defender, SpecialConditions.CONFUSED):
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="08188be3-c523-5e00-be37-3a450ddea121",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Attack(
            title="Perplex",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Brain Crush",
            game_text="If your opponent's Active Pokémon isn't Confused, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=130,
            effect=brain_crush,
        ),
    ],
)
