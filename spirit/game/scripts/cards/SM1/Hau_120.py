"""Hau (SM - Celestial Storm 132/168 -- JP SM7 090/096).

Supporter.

  "Draw 3 cards."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="f471107c-e923-58bd-830c-34517922bfad",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hau.Name",
    display_name="Hau",
    searchable_by=["Hau", "Supporter", "Hau"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=draw_attack(3),
)
