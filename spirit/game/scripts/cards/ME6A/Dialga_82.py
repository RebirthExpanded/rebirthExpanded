"""Dialga (ME6A 82 -- JP M6a 082; English 30C/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def reversed_clock(ctx):
    pool = [c for c in ctx.recoverable_discard() if is_pokemon_card(c) or is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(3, len(pool)), minimum=0,
                                   prompt="Choose up to 3 Pokémon and Basic Energy cards to shuffle into your deck.")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


card = PokemonCardDef(
    guid="27f4b2b5-fab1-5272-acf9-6ad0719f8dca",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=483,
    abilities=[
        Attack(
            title="Reversed Clock",
            game_text="Shuffle up to 3 in any combination of Pokémon and Basic Energy cards from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=reversed_clock,
        ),
        Attack(
            title="Heavy Impact",
            game_text="",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
