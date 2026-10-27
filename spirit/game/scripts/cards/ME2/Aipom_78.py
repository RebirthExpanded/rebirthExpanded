"""Aipom (ME2 78 -- JP M2 066; English PFL/78). Japanese art.
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


async def astonish(ctx):
    await ctx.deal_damage()
    await _random_hand_to_deck(ctx, 1)


card = PokemonCardDef(
    guid="67df3708-9719-5b66-8c55-f927e42b280c",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=["Aipom", "Basic"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=190,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Choose a random card from your opponent's hand, and your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=astonish,
        ),
    ],
)
