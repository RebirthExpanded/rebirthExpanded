"""Eri (SV - Temporal Forces 146/162 -- JP SV5K 067/071).

Supporter.

  "Your opponent reveals their hand, and you discard up to 2 Item cards you find there."

Playable with any card in their hand: the reveal is the effect even
when no Item turns up. Pokemon Tools are not Items here, so a Tool in
their hand is safe.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import eri, eri_condition
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="8a883cb3-cae4-5aaa-a0c1-a8bfbd54f449",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eri.Name",
    display_name="Eri",
    searchable_by=["Eri", "Supporter", "Eri"],
    subtypes=["Supporter"],
    collector_number=146,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=eri,
    condition=eri_condition,
)
