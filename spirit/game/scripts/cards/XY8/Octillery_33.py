"""Octillery (XY - BREAKthrough 33/162 -- JP XY8-Bb 015/059).

Stage 1 Water Pokemon, evolves from Remoraid. HP 90, weakness Grass x2,
retreat 2.

  Ability  Abyssal Hand  Once during your turn (before your attack), you may
                         draw cards until you have 5 cards in your hand.
  Hug  [WWC] 40  The Defending Pokemon can't retreat during your opponent's
                 next turn.

Not offered with 5 or more already in hand (nothing to draw).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)


def _hand_below_five(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return len(hand.children if hand else []) < 5


async def hug(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


card = PokemonCardDef(
    guid="21bea03b-2b77-5874-b076-ade8b3261556",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Ability(
            title="Abyssal Hand",
            game_text="Once during your turn (before your attack), you may draw cards until you have 5 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_hand_below_five,
            effect=draw_until_effect(5),
        ),
        Attack(
            title="Hug",
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=hug,
        ),
    ],
)
