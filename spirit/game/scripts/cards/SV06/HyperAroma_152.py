"""Hyper Aroma (SV - Twilight Masquerade 152/167 -- JP SV5a).

Item, ACE SPEC.

  "Search your deck for up to 3 Stage 1 Pokemon, reveal them, and put them
   into your hand. Then, shuffle your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_stage1_pokemon



def _deck_not_empty(board, player_id, card=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


card = ItemCardDef(
    guid="8a244b2e-f6e7-5fd0-a479-c07a6f95b326",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HyperAroma.Name",
    display_name="Hyper Aroma",
    searchable_by=['Hyper Aroma', 'Item', 'ACE SPEC', 'HyperAroma'],
    subtypes=['Item', 'ACE SPEC'],
    collector_number=152,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Ace,
    condition=_deck_not_empty,
    effect=search_to_hand(is_stage1_pokemon, count=3, minimum=0, reveal=True,
                          prompt="Choose up to 3 Stage 1 Pokémon to put into your hand."),
)
