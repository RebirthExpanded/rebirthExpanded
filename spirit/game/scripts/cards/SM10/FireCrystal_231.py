"""Fire Crystal (SM - Unbroken Bonds 173/214 -- JP SM10 087/095).

Item.

  "Put 3 Fire Energy cards from your discard pile into your hand."

Superior Energy Retrieval for one type: playable with at least one [R]
Energy in the discard, taking up to 3.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import (recover_from_discard,
                                                      requires_discard)
from spirit.game.card_effects.trainers import is_fire_energy_card
from spirit.game.data_utils import ItemCardDef

card = ItemCardDef(
    guid="3e059737-81d7-5c70-89fb-9acba4c54819",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireCrystal.Name",
    display_name="Fire Crystal",
    searchable_by=["Fire Crystal", "Item", "FireCrystal"],
    subtypes=["Item"],
    collector_number=231,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    effect=recover_from_discard(
        is_fire_energy_card, count=3, minimum=1,
        prompt="Choose up to 3 Fire Energy cards to put into your hand."),
    condition=requires_discard(is_fire_energy_card, 1),
)
