"""Dizzying Valley (ME - Phantasmal Flames 88 -- JP M2 080/080).

Stadium.

  "Confused Pokemon (both yours and your opponent's) don't recover from that
   Special Condition when they evolve or devolve."

The keeps_confusion_through_evolution hook: the evolve and devolve paths
re-mark the new top card Confused after the usual wipe.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef
from spirit.game.session.passives import Passive


class DizzyingValleyPassive(Passive):
    def keeps_confusion_through_evolution(self, pokemon, carrier):
        return True


card = StadiumCardDef(
    guid="ee52e013-08fb-57f3-bfe6-cfb3983ba4bb",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DizzyingValley.Name",
    display_name="Dizzying Valley",
    searchable_by=["Dizzying Valley", "Stadium", "DizzyingValley"],
    subtypes=["Stadium"],
    collector_number=88,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=DizzyingValleyPassive(),
)
