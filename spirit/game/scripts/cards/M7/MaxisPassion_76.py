"""Maxi's Passion (M7 76 -- JP M7 076/078 マキシの熱血). Japanese art.

Provisional English name and text (no English release yet).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, Activations, SupporterCardDef, Triggers
from spirit.game.card_effects import m7


card = SupporterCardDef(
    guid="3e00afe5-7b69-5db2-8009-72eb5084d19e",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxisPassion.Name",
    display_name="Maxi's Passion",
    searchable_by=["Maxi's Passion", 'Supporter', 'MaxisPassion'],
    subtypes=['Supporter'],
    collector_number=76,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    condition=m7.maxis_passion_condition,
    effect=m7.maxis_passion,
)
