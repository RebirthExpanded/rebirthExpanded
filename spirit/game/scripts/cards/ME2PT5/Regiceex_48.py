"""Regice ex (ME2PT5 48 -- JP MC 192; English ASC/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card
from spirit.game.card_effects import support_common as su


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)


regi_charge = su.attach_from_discard(
    _basic_water, count=2, target="self", minimum=0,
    prompt="Attach up to 2 Basic Water Energy cards from your discard pile to this Pokémon.")


async def ice_prison(ctx):
    await ctx.deal_damage()
    await ctx.discard_energy_units_from(ctx.attacker, 2, prompt="Choose 2 Energy to discard from this Pokémon", partial=True)
    target = ctx.opponent_active()
    if target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="d119831b-9fc2-55bf-8f18-6911c6edfcbc",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regiceex.Name",
    display_name="Regice ex",
    searchable_by=["Regice ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=48,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Attack(
            title="Regi Charge",
            game_text="Attach up to 2 Basic Water Energy cards from your discard pile to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=regi_charge,
        ),
        Attack(
            title="Ice Prison",
            game_text="Discard 2 Energy from this Pokémon, and your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=ice_prison,
        ),
    ],
)
