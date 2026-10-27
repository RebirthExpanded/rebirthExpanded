"""Friends in Paldea (SV085 109 -- JP SV8a 174; English PRE/109, PRE/137). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects import support_common as su


card = SupporterCardDef(
    guid="c4fdbf0b-e3c0-5cc2-8b6a-7969f6b8cd5b",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendsinPaldea.Name",
    display_name="Friends in Paldea",
    searchable_by=["Friends in Paldea", "Supporter"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=su.draw_attack(3),
)
