"""Nemona (SVPJ 153 -- JP SVP 153; English PAF/229, PAF/238, PAF/82, SVI/180). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects import support_common as su


card = SupporterCardDef(
    guid="0e8493eb-a33f-55b0-9cc9-70986353d89f",
    key="SVPJ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nemona.Name",
    display_name="Nemona",
    searchable_by=["Nemona", "Supporter"],
    subtypes=["Supporter"],
    collector_number=153,
    set_code="SVPJ",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    effect=su.draw_attack(3),
)
