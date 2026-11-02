"""Polteageist V (Promo_SWSH 21 -- JP SP 040; English SP/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

import random

from spirit.game.card_effects import passives_common as pc


async def _teapot_of_surprises(ctx):
    """Put a random card from the attacker's hand on the bottom of their deck, revealed."""
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    card = random.choice(hand)
    await ctx.reveal_cards([card])
    await ctx.put_on_bottom_of_deck(card)


card = PokemonCardDef(
    guid="c1aa3ebd-cdff-5444-af19-68cda3193a74",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PolteageistV.Name",
    display_name="Polteageist V",
    searchable_by=["Polteageist V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=21,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RareHoloV,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=855,
    abilities=[
        Ability(
            title="Teapot of Surprises",
            game_text="If this Pokémon is in the Active Spot and is damaged by an opponent's attack (even if it is Knocked Out), choose a random card from your opponent's hand. Your opponent reveals that card and puts it on the bottom of their deck.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=_teapot_of_surprises,
        ),
        Attack(
            title="Mind Bend",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
