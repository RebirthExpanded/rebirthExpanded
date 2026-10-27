"""Black Kyurem ex (SV08 48 -- JP SV7a 011; English SSP/218, SSP/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


async def ice_age(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and d not in ctx.knockouts and _of_type(d, PokemonTypes.DRAGON):
        await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="341ff453-4bd1-5403-b826-622ee04f2d34",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyuremex.Name",
    display_name="Black Kyurem ex",
    searchable_by=["Black Kyurem ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=48,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Ice Age",
            game_text="If your opponent's Active Pokémon is a Dragon Pokémon, it is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=ice_age,
        ),
        Attack(
            title="Black Frost",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=250,
            effect=ac.recoil_attack(30),
        ),
    ],
)
