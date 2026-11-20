"""Reporter (M7 77 -- JP M7 077/078 レポーター). Japanese art.

Provisional English name and text (no English release yet).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, Activations, SupporterCardDef, Triggers
from spirit.game.card_effects import m7


card = SupporterCardDef(
    guid="bf492619-be2c-57f4-92ed-8d262afad617",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Reporter.Name",
    display_name='Reporter',
    searchable_by=['Reporter', 'Supporter', 'Reporter'],
    subtypes=['Supporter'],
    collector_number=77,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=m7.reporter,
)
