"""Toxtricity (SV1 72 -- JP SV1V 032; English SVI/72). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

import random


async def _random_hand_to_deck(ctx, count):
    hand = list(ctx.hand(ctx.opponent_id))
    picks = random.sample(hand, min(count, len(hand)))
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def yank_away(ctx):
    await _random_hand_to_deck(ctx, 2)


card = PokemonCardDef(
    guid="2bbd9e25-794a-57c3-a546-d9f9433a001b",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Yank Away",
            game_text="Choose 2 random cards from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=yank_away,
        ),
        Attack(
            title="Thunder",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=ac.recoil_attack(20),
        ),
    ],
)
