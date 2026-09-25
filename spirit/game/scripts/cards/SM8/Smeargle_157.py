"""Smeargle (SM - Lost Thunder 157/214 -- JP SM8 070/095).

Basic Colorless Pokemon. HP 80, weakness Fighting x2, retreat 1.

  Stunning Likeness  [C]     Your opponent reveals their hand. You may use
                             the effect of a Supporter card you find there as
                             the effect of this attack.
  Tail Smash         [C] 30  Flip a coin. If tails, this attack does nothing.

Oranguru (CZ)'s Primate Acting shape, reading the hand instead of the
discard pile. The Supporter stays in the opponent's hand.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.data_utils import TRAINER_EFFECTS_BY_GUID, unimplemented
from spirit.game.session.effects import is_supporter_card
from spirit.game.data_utils import Attack, PokemonCardDef


def _runnable_supporter(card) -> bool:
    if not is_supporter_card(card):
        return False
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    return effect is not None and effect is not unimplemented


async def stunning_likeness(ctx):
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    candidates = [c for c in hand if _runnable_supporter(c)]
    if not candidates:
        return
    picked = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="You may choose a Supporter card to use its effect")
    if not picked:
        return
    await TRAINER_EFFECTS_BY_GUID[(picked[0].archetype_id or "").lower()](ctx)


card = PokemonCardDef(
    guid="41c70a7b-fd91-5862-bd04-4b1e430280c6",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=['Smeargle', 'Basic', 'Smeargle'],
    subtypes=['Basic'],
    collector_number=157,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Attack(title="Stunning Likeness", game_text="Your opponent reveals their hand. You may use the effect of a Supporter card you find there as the effect of this attack.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=stunning_likeness),
        Attack(title="Tail Smash", game_text="Flip a coin. If tails, this attack does nothing.",
               cost={PokemonTypes.COLORLESS: 1}, damage=30,
               effect=flip_or_nothing()),
    ],
)
