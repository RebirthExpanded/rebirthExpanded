"""Master Ball (BW - Plasma Blast 94/101 -- JP KK 017).

Item, ACE SPEC.

  "Search your deck for a Pokemon, reveal it, and put it into your hand.
   Shuffle your deck afterward."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_pokemon_card


def _deck_not_empty(board, player_id, card=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


card = ItemCardDef(
    guid="05b79847-7185-51ae-a8b4-1eda9a491708",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item", "ACE SPEC", "MasterBall"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=94,
    set_code="BW10",
    rarity=Rarities.Ace,
    condition=_deck_not_empty,
    effect=search_to_hand(is_pokemon_card, count=1, reveal=True,
                          prompt="Choose a Pokémon to put into your hand."),
)
