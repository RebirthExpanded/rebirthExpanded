"""Tierno (JP XY Hyper Metal Chain Deck 60 -- HMC 015/018; English print
XY - Phantom Forces 107/119).

Supporter.

  "Draw 3 cards."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack, requires_deck
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="51bf83d8-fb5e-5195-a435-4573c2dda5ec",
    key="HMC",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tierno.Name",
    display_name="Tierno",
    searchable_by=["Tierno", "Supporter"],
    subtypes=["Supporter"],
    collector_number=15,
    set_code="HMC",
    rarity=Rarities.Uncommon,
    condition=requires_deck(1),
    effect=draw_attack(3),
)
