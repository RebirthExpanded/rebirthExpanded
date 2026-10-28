"""Krabby (SV035 98 -- JP SV2a 098; English MEW/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)


async def salt_water(ctx):
    results = await ctx.flip_coins(1, "Salt Water")
    if results and results[0]:
        picks = await ctx.search_deck(_basic_water, count=2, minimum=0, prompt="Choose up to 2 Basic Water Energy cards to attach")
        for card in picks:
            await ctx.attach_energy(card, ctx.attacker)
        await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="841d8e99-2a80-5317-9218-ad577e1b7084",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    display_name="Krabby",
    searchable_by=["Krabby", "Basic"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=98,
    abilities=[
        Attack(
            title="Salt Water",
            game_text="Flip a coin. If heads, search your deck for up to 2 Basic Water Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=salt_water,
        ),
        Attack(
            title="Crabhammer",
            game_text="",
            cost={PokemonTypes.WATER: 3},
            damage=50,
        ),
    ],
)
