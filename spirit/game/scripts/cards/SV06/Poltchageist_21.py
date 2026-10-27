"""Poltchageist (SV06 21 -- JP SV6 013; English TWM/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


async def tea_server(ctx):
    pool = [c for c in ctx.discard_pile() if _basic_grass(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Grass Energy card")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="9fbed3bc-2c02-501d-8bea-878253e0d1d2",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    display_name="Poltchageist",
    searchable_by=["Poltchageist", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1012,
    abilities=[
        Attack(
            title="Tea Server",
            game_text="Put a Basic Grass Energy card from your discard pile into your hand.",
            cost={PokemonTypes.GRASS: 1},
            effect=tea_server,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
