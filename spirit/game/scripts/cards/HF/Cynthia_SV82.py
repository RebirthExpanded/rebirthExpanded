"""Cynthia (SM - Ultra Prism 119/156 -- JP SM5M 061/066).

Supporter.

  "Shuffle your hand into your deck. Then, draw 6 cards."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="68a06f33-f721-5452-a4c5-0bb6e64f675e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter", "Cynthia"],
    subtypes=["Supporter"],
    collector_number=151,
    set_code="HF",
    rarity=Rarities.RareUltra,
    effect=shuffle_hand_into_deck_draw(6),
)
