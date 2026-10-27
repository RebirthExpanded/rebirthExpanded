"""Okidogi ex (SV065 36 -- JP SV6a 036; English SFA/36, SFA/82, SFA/90). Japanese art.
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
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_darkness(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.DARKNESS)


async def poisonous_musculature(ctx):
    picks = await ctx.search_deck(_basic_darkness, count=2, minimum=0,
                                  prompt="Choose up to 2 Basic Darkness Energy cards to attach to this Pokémon.")
    attached = 0
    for card in picks:
        if await ctx.attach_energy(card, ctx.attacker):
            attached += 1
    await ctx.shuffle_deck()
    if attached:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.POISONED)


def _self_poisoned(ctx) -> bool:
    return _has_condition(ctx.attacker, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="5fcad1d7-f40b-5432-ad85-23fba204cecf",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Okidogiex.Name",
    display_name="Okidogi ex",
    searchable_by=["Okidogi ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=36,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1014,
    abilities=[
        Attack(
            title="Poisonous Musculature",
            game_text="Search your deck for up to 2 Basic Darkness Energy cards and attach them to this Pokémon. Then, shuffle your deck. If you attached Energy to a Pokémon in this way, this Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=poisonous_musculature,
        ),
        Attack(
            title="Chain-Crazed",
            game_text="If this Pokémon is Poisoned, this attack does 130 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=ac.bonus_if(_self_poisoned, 130),
        ),
    ],
)
