"""Professor Juniper (Black & White 101/114 -- JP BW1-Bb 049/053).

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
    guid="6f46a793-9360-5f80-90db-a68731006d24",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorJuniper.Name",
    display_name="Professor Juniper",
    searchable_by=["Professor Juniper", "Supporter", "ProfessorJuniper"],
    subtypes=["Supporter"],
    collector_number=101,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=professors_research,
)
