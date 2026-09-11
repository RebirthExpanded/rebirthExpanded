"""Fiery Torch (XY - Flashfire 89/106 -- JP XY2 073/080).

Item.

  "Discard a Fire Energy card from your hand. (If you can't discard a Fire Energy card, you can't play this card.) Draw 2 cards."

The parenthetical is a playability condition: no [R] Energy in hand,
no Torch. The discard itself is mandatory once played.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import (discard_then_draw,
                                                      requires_hand)
from spirit.game.card_effects.trainers import is_fire_energy_card
from spirit.game.data_utils import ItemCardDef

card = ItemCardDef(
    guid="cb313d31-7a65-59f9-829c-2d69fba0d456",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieryTorch.Name",
    display_name="Fiery Torch",
    searchable_by=["Fiery Torch", "Item", "FieryTorch"],
    subtypes=["Item"],
    collector_number=89,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    effect=discard_then_draw(
        1, 2, optional=False, predicate=is_fire_energy_card,
        prompt="Choose a Fire Energy card to discard."),
    condition=requires_hand(is_fire_energy_card, 1, exclude_self=False),
)
