"""Chien-Pao (SV4 57 -- JP SV4M 021; English PAR/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)


async def _discard_to_one(ctx, pred, upto, label):
    pool = [c for c in ctx.discard_pile() if pred(c)]
    if not pool:
        return
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon")
    if target is None:
        return
    picks = await ctx.choose_cards(pool, min(upto, len(pool)), minimum=0, prompt=f"Attach up to {upto} {label}")
    for card in picks:
        await ctx.attach_energy(card, target)


async def snow_bringer(ctx):
    await _discard_to_one(ctx, _basic_water, 2, "Basic Water Energy cards")


card = PokemonCardDef(
    guid="bd462221-be45-5192-bb19-33e2d3e6f392",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChienPao.Name",
    display_name="Chien-Pao",
    searchable_by=["Chien-Pao", "Basic"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=1002,
    abilities=[
        Attack(
            title="Snow Bringer",
            game_text="Attach up to 2 Basic Water Energy cards from your discard pile to 1 of your Pokémon.",
            cost={PokemonTypes.WATER: 1},
            effect=snow_bringer,
        ),
        Attack(
            title="Wrathful Blade",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
