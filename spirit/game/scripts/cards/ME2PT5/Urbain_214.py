"""Urbain (ME2PT5 214 -- JP MC 702; English ASC/214). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects import support_common as su


card = SupporterCardDef(
    guid="bb2eca41-1df6-5cdb-80d5-bf76ac1f68b8",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Urbain.Name",
    display_name="Urbain",
    searchable_by=["Urbain", "Supporter"],
    subtypes=["Supporter"],
    collector_number=214,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=su.draw_attack(3),
)
