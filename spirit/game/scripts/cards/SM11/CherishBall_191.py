"""Cherish Ball (SM - Unified Minds 191/236 -- JP SM12a 168/173).

Item.

  "Search your deck for a Pokemon-GX, reveal it, and put it into your hand.
   Then, shuffle your deck."

Pokemon-GX only, at any stage: the GX subtype is what the search reads, so
a TAG TEAM is a target and a Pokemon-EX is not.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import is_pokemon_gx
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_pokemon_card


def _is_pokemon_gx_card(card) -> bool:
    return is_pokemon_card(card) and is_pokemon_gx(card.archetype_id)


card = ItemCardDef(
    guid="c41c294f-b1b2-5cdc-a6db-609be875f4b4",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CherishBall.Name",
    display_name="Cherish Ball",
    searchable_by=["Cherish Ball", "Item", "CherishBall"],
    subtypes=["Item"],
    collector_number=191,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _is_pokemon_gx_card, count=1, minimum=0,
        prompt="Choose a Pokémon-GX to put into your hand."),
)
