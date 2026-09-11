"""Oranguru (SM - Sun & Moon 113/149 -- JP SM1M 040/060).

Basic Colorless Pokemon. HP 120, weakness Fighting x2, retreat 2.

  Ability  Instruct  Once during your turn (before your attack), you may
                     draw cards until you have 3 cards in your hand.
  Psychic  [CCC] 60+  This attack does 20 more damage for each Energy
                      attached to your opponent's Active Pokemon.

Not offered with 3 or more already in hand. Psychic counts Energy CARDS
(a Double Colorless is one).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)


def _hand_below_three(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return len(hand.children if hand else []) < 3 \
        and bool(deck and deck.children)


card = PokemonCardDef(
    guid="d90b422e-5fda-54e5-9ce7-2ab0f6ba1450",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name",
    display_name="Oranguru",
    searchable_by=["Oranguru", "Basic"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="SM1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=765,
    abilities=[
        Ability(
            title="Instruct",
            game_text="Once during your turn (before your attack), you may draw cards until you have 3 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_hand_below_three,
            effect=draw_until_effect(3),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=damage_per(count_energy("defender", cards=True), 20, base=60),
        ),
    ],
)
