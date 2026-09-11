"""Ball Guy (SWSH - Shining Fates 65/72; the full-art print of 57).

Supporter.

  "Search your deck for up to 3 different Item cards with 'Ball' in their
   name, reveal them, and put them into your hand. Then, shuffle your deck."

The two prints are the same card; the behaviour lives in card_effects.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import ball_guy
from spirit.game.data_utils import SupporterCardDef


card = SupporterCardDef(
    guid="781b22f5-be57-549e-a72e-3380392bf826",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BallGuy.Name",
    display_name="Ball Guy",
    searchable_by=["Ball Guy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=65,
    set_code="SWSH45",
    rarity=Rarities.RareUltra,
    effect=ball_guy,
)
