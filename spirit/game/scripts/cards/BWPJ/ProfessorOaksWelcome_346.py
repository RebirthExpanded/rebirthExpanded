"""Professor Oak's Welcome (BWPJ 346 -- JP WAK 046; English Japan only). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects import support_common as su


card = SupporterCardDef(
    guid="1a96c168-4c4e-5af1-a926-4cb869099510",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksWelcome.Name",
    display_name="Professor Oak's Welcome",
    searchable_by=["Professor Oak's Welcome", "Supporter"],
    subtypes=["Supporter"],
    collector_number=346,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    effect=su.draw_attack(2),
)
