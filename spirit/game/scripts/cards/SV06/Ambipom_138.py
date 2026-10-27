"""Ambipom (SV06 138 -- JP SV6 087; English TWM/138). Japanese art.
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


async def wicked_tail(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if not ctx.hand(ctx.opponent_id) or not await ctx.ask_yes_no("Use Wicked Tail?"):
        return
    heads = sum(1 for r in await ctx.flip_coins(2, "Wicked Tail") if r)
    if heads:
        await _random_hand_to_deck(ctx, heads)


card = PokemonCardDef(
    guid="ca219103-734e-5a11-ba7a-8d1ba0e7d5fa",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name",
    display_name="Ambipom",
    searchable_by=["Ambipom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=138,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    family_id=190,
    abilities=[
        Ability(
            title="Wicked Tail",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may flip 2 coins. For each heads, choose a random card from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=wicked_tail,
        ),
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
