"""Lusamine (SM - Crimson Invasion 96/111).

Supporter.

  "Put 2 in any combination of Supporter and Stadium cards from your
   discard pile into your hand."

"2 in any combination" is one pick of 2 over both card types at once, not
two separate picks, so recover_from_discard runs a single browser holding
the Supporters and the Stadiums together. With only one there, that one
comes back.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import (recover_from_discard,
                                                     requires_discard)
from spirit.game.session.effects import is_stadium_card, is_supporter_card


def _supporter_or_stadium(card):
    return is_supporter_card(card) or is_stadium_card(card)


card = SupporterCardDef(
    guid="7c45dfe6-5aad-5354-be04-2337ef1c619b",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name",
    display_name="Lusamine",
    searchable_by=["Lusamine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=96,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(
        _supporter_or_stadium, count=2, minimum=1, reveal=True, to="hand",
        prompt="Choose 2 Supporter or Stadium cards to put into your hand.",
    ),
    condition=requires_discard(_supporter_or_stadium, 1),
)
