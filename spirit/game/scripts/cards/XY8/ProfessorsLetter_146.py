"""Professor's Letter (XY - BREAKthrough 146/162 -- JP 20th 056/072).

Item.

  "Search your deck for up to 2 basic Energy cards, reveal them, and put
   them into your hand. Shuffle your deck afterward."

The plainest search in the family: search_to_hand with the basic-Energy
filter, "up to 2" as minimum=0. Special Energy is not basic Energy, so a
Double Colorless in the deck is not a candidate.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_basic_energy

card = ItemCardDef(
    guid="0df8dfdb-eee2-505f-9221-48a0c5a7cde6",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsLetter.Name",
    display_name="Professor's Letter",
    searchable_by=["Professor's Letter", "Item", "ProfessorsLetter"],
    subtypes=["Item"],
    collector_number=146,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        is_basic_energy, count=2, minimum=0,
        prompt="Choose up to 2 basic Energy cards to put into your hand."),
)
