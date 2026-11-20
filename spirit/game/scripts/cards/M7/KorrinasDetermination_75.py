"""Korrina's Determination (M7 75 -- JP M7 075/078 コルニの本気). Japanese art.

Provisional English name and text (no English release yet).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, Activations, SupporterCardDef, Triggers
from spirit.game.card_effects import m7


card = SupporterCardDef(
    guid="2e0880bc-4107-5e2f-b650-bf993a7028fc",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KorrinasDetermination.Name",
    display_name="Korrina's Determination",
    searchable_by=["Korrina's Determination", 'Supporter', 'KorrinasDetermination'],
    subtypes=['Supporter'],
    collector_number=75,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=m7.korrinas_determination,
)
