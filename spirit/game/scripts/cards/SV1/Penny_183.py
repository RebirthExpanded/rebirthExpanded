"""Penny (SV - Scarlet & Violet 183/198 -- JP SV1S 073/078).

Supporter.

  "Put 1 of your Basic Pokemon and all attached cards into your hand."

Acerola without the damage requirement and with a stage requirement
instead. "Your Basic Pokemon" is the Pokemon in play, i.e. the top card of
the pile: a Basic sitting under an evolution is not one, so an evolved
Pokemon cannot be picked up with this.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import penny, penny_condition
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="51d4322f-9657-548f-9f0b-7c3608a2a6dd",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Penny.Name",
    display_name="Penny",
    searchable_by=["Penny", "Supporter"],
    subtypes=["Supporter"],
    collector_number=183,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=penny,
    condition=penny_condition,
)
