"""Cynthia (SM - Ultra Prism 119/156 -- JP SM5M 061/066).

Supporter.

  "Shuffle your hand into your deck. Then, draw 6 cards."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="72ce19ae-e033-5466-9f92-5a96839bc8a6",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter", "Cynthia"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_into_deck_draw(6),
)
