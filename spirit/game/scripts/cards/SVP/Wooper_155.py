"""Wooper (SVP 155 -- JP SVP 121; English SVP/155). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)


async def scoop_water(ctx):
    pool = [c for c in ctx.discard_pile() if _basic_water(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(3, len(pool)), minimum=0, prompt="Shuffle up to 3 Basic Water Energy cards into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


card = PokemonCardDef(
    guid="1c0a6326-9fbd-56f5-94f1-7351b4b65b6f",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    display_name="Wooper",
    searchable_by=["Wooper", "Basic"],
    subtypes=["Basic"],
    collector_number=155,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=194,
    abilities=[
        Attack(
            title="Scoop Water",
            game_text="Shuffle up to 3 Basic Water Energy cards from your discard pile into your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=scoop_water,
        ),
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
