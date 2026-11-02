"""Well-rounded Musician (SPJ 119 -- JP SP 119; English Japan only). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects.trainers import hop


card = SupporterCardDef(
    guid="63f797b3-8abe-5bba-a3e8-e566fd2d566d",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WellroundedMusician.Name",
    display_name="Well-rounded Musician",
    searchable_by=["Well-rounded Musician", "Supporter"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="SPJ",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    effect=hop,
)
