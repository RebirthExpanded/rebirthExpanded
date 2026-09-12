"""Tera Orb (SV - Surging Sparks 189/191 -- JP SV8a 145/187, the art here).

Item.

  "Search your deck for a Tera Pokemon, reveal it, and put it into your
   hand. Then, shuffle your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_deck, search_to_hand
from spirit.game.data_utils import ItemCardDef, subtypes_for


def _is_tera_card(card) -> bool:
    return "Tera" in subtypes_for(card.archetype_id)


card = ItemCardDef(
    guid="0f221df1-fc08-518e-aea8-4db6cd09bd40",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeraOrb.Name",
    display_name="Tera Orb",
    searchable_by=["Tera Orb", "Item", "TeraOrb"],
    subtypes=["Item"],
    collector_number=189,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=requires_deck(1),
    effect=search_to_hand(_is_tera_card, count=1, minimum=0, reveal=True,
                          prompt="Choose a Tera Pokémon to put into your hand."),
)
