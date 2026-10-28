"""Wartortle (SV035 8 -- JP SV2a 008; English MEW/171, MEW/8). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)


async def free_diving(ctx):
    pool = [c for c in ctx.discard_pile() if _basic_water(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(3, len(pool)), minimum=0, prompt="Choose up to 3 Basic Water Energy cards")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="054fcfdc-ed21-5837-ab0d-e3df9ca0e76c",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    display_name="Wartortle",
    searchable_by=["Wartortle", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    family_id=7,
    abilities=[
        Attack(
            title="Free Diving",
            game_text="Put up to 3 Basic Water Energy cards from your discard pile into your hand.",
            cost={PokemonTypes.WATER: 1},
            effect=free_diving,
        ),
        Attack(
            title="Spinning Attack",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=50,
        ),
    ],
)
