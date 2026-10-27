"""Influencer's Presentation (MP1 19 -- JP MP1 019; English Japan only). Japanese art.

While introducing your favorite Pokémon to your opponent, draw 3 cards. (If your opponent liked it, they may say "Like!")
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects import support_common as su


card = SupporterCardDef(
    guid="81211b96-b71b-597a-823f-91f417a9f2d3",
    key="MP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.InfluencersPresentation.Name",
    display_name="Influencer's Presentation",
    searchable_by=["Influencer's Presentation", "Supporter"],
    subtypes=["Supporter"],
    collector_number=19,
    set_code="MP1",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    effect=su.draw_attack(3),
)
