"""Professor Sycamore (XY 122/146 -- JP "THE BEST OF XY" 2017).

Supporter.

  "Discard your hand and draw 7 cards."

The same card as Professor's Research under an earlier name, and the
deck-building rule that goes with that: a deck may hold copies of only one
of Professor's Research, Professor Sycamore and Professor Juniper, which
rules.EXCLUSIVE_NAME_GROUPS enforces the way it does for Boss's Orders and
Lysandre.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="25cbfa51-44a7-5d0e-b7f1-a1e1a7d79659",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorSycamore.Name",
    display_name="Professor Sycamore",
    searchable_by=["Professor Sycamore", "Supporter", "ProfessorSycamore"],
    subtypes=["Supporter"],
    collector_number=122,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=professors_research,
)
