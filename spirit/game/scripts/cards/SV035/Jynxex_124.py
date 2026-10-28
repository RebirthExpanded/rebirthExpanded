"""Jynx ex (SV035 124 -- JP SV2a 124; English MEW/124, MEW/191). Japanese art.
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


async def heart_stopping_kiss(ctx):
    d = ctx.opponent_active()
    if d is not None and not ctx.effects_blocked(d) and _has_condition(d, SpecialConditions.ASLEEP):
        await ctx.knock_out(d)


card = PokemonCardDef(
    guid="d4ca223c-7fa7-5376-afc1-9a07a583feb6",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynxex.Name",
    display_name="Jynx ex",
    searchable_by=["Jynx ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=124,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=238,
    abilities=[
        Attack(
            title="Heart-Stopping Kiss",
            game_text="If your opponent's Active Pokémon is Asleep, it is Knocked Out.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=heart_stopping_kiss,
        ),
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
