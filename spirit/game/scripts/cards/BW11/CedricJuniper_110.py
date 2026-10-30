"""Cedric Juniper (BW - Legendary Treasures 110/113).

  "Put a Pokemon from your hand face down in front of you and tell your
   opponent its name. Your opponent guesses the height of that Pokemon.
   Flip the Pokemon over. If your opponent guessed right, he or she draws 3
   cards. If your opponent guessed wrong, you draw 3 cards. Return the
   Pokemon to your hand. (You may look at the height of your Pokemon.)"

Only a Pokemon card that prints a height can be chosen (support_common's
printed_height: no rule-box cards, nothing newer than Sun & Moon).
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import (
    cedric_juniper,
    cedric_juniper_condition,
)

card = SupporterCardDef(
    guid="159594b4-73d7-5ec8-a1f4-2144c651e3cd",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CedricJuniper.Name",
    display_name="Cedric Juniper",
    searchable_by=["Cedric Juniper", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    effect=cedric_juniper,
    condition=cedric_juniper_condition,
)
