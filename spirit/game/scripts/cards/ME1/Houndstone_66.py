"""Houndstone (ME1 66 -- JP M1S 048; English MEG/145, MEG/66). Japanese art.
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


async def horrifying_bite(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails("Horrifying Bite")
    if heads:
        await _random_hand_to_deck(ctx, heads)


card = PokemonCardDef(
    guid="677a9ea9-f968-5798-a22d-6ead171e27df",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndstone.Name",
    display_name="Houndstone",
    searchable_by=["Houndstone", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    family_id=971,
    abilities=[
        Attack(
            title="Horrifying Bite",
            game_text="Flip a coin until you get tails. For each heads, choose a random card from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=horrifying_bite,
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
