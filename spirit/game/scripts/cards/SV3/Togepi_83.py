"""Togepi (SV3 83 -- JP SV3 043; English OBF/83). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

import random


async def _random_hand_to_deck(ctx, count):
    hand = list(ctx.hand(ctx.opponent_id))
    picks = random.sample(hand, min(count, len(hand)))
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def whiny_voice(ctx):
    await _random_hand_to_deck(ctx, 1)


card = PokemonCardDef(
    guid="8cf18c8a-7e45-52d5-adad-f9d09df0e7da",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    display_name="Togepi",
    searchable_by=["Togepi", "Basic"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=175,
    abilities=[
        Attack(
            title="Whiny Voice",
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=whiny_voice,
        ),
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
