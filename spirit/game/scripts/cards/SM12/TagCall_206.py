"""Tag Call (SM - Cosmic Eclipse 206/236).

Item.

  "Search your deck for up to 2 TAG TEAM cards, reveal them, and put them
   into your hand. Then, shuffle your deck."

"TAG TEAM cards", not TAG TEAM Pokemon: the subtype also sits on the
TAG TEAM Supporters (Guzma & Hala, Cynthia & Caitlin, Red & Blue and the
rest of the Cosmic Eclipse set), and this fetches those too. So the
predicate reads the subtype off the definition and asks nothing about the
card being a Pokemon.

Today the pool holds exactly one card it can find, Naganadel &
Guzzlord-GX. That is a property of the pool, not of this card, and it is
why the predicate is written against the subtype rather than a list --
every TAG TEAM added later is found without touching this file.

No condition. Like Nest Ball and the other search Items it costs nothing,
so it is playable even when the deck holds nothing to find; "up to 2" is
minimum=0, which lets the player take one or none.
"""

from spirit.game.data_utils import ItemCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand


def is_tag_team(card) -> bool:
    """Any card with the TAG TEAM subtype -- Pokemon or Supporter."""
    return "TAG TEAM" in subtypes_for(card.archetype_id)


tag_call = search_to_hand(
    is_tag_team, count=2, minimum=0, reveal=True,
    prompt="Choose up to 2 TAG TEAM cards to put into your hand.",
)


card = ItemCardDef(
    guid="04a9f03e-8f5c-5b8d-a5a2-661a1dc0ed92",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TagCall.Name",
    display_name="Tag Call",
    searchable_by=["Tag Call", "Item", "TagCall"],
    subtypes=["Item"],
    collector_number=206,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=tag_call,
)
