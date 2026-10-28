"""Toedscool (SV4 15 -- JP SV4M 006; English PAR/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


async def clinging_spore(ctx):
    pool = [c for c in ctx.hand() if _basic_grass(c)]
    bench = ctx.my_bench()
    if not pool or not bench:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Grass Energy card to attach")
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon") if picks else None
    if target is not None:
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="39f8bef1-c0a8-5ebd-b961-1fd7d98c733e",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    display_name="Toedscool",
    searchable_by=["Toedscool", "Basic"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=948,
    abilities=[
        Attack(
            title="Clinging Spore",
            game_text="Attach a Basic Grass Energy card from your hand to 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=clinging_spore,
        ),
        Attack(
            title="Vine Slap",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
