"""Hau (SM - Celestial Storm 132/168 -- JP SM7 090/096).

Supporter.

  "Draw 3 cards."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="c6a9dcfc-c8bc-5001-b7bc-918e70514534",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hau.Name",
    display_name="Hau",
    searchable_by=["Hau", "Supporter", "Hau"],
    subtypes=["Supporter"],
    collector_number=132,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=draw_attack(3),
)
