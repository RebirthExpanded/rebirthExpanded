"""Primeape (SV035 57 -- JP SV2a 057; English MEW/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.attributes import SpecialConditions


def _has_condition(pokemon, *conditions) -> bool:
    have = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [] if pokemon is not None else []
    return any(CLIENT_SPECIAL_CONDITION_NAMES[c] in have for c in conditions)


async def rant_and_rave(ctx):
    await ctx.deal_damage()
    if ctx.attacker not in ctx.knockouts:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


async def raging_smash(ctx):
    if _has_condition(ctx.attacker, SpecialConditions.CONFUSED):
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="20707ec1-eaad-54a0-b7e6-74ef2da1a8ac",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Rant and Rave",
            game_text="This Pokémon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=rant_and_rave,
        ),
        Attack(
            title="Raging Smash",
            game_text="If this Pokémon isn't Confused, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=raging_smash,
        ),
    ],
)
