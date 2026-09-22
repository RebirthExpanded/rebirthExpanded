"""Apricorn Maker (SM - Celestial Storm 124/168 -- JP SM6b 063/066, the art here).

Supporter.

  "Search your deck for up to 2 Item cards that have 'Ball' in their name,
   reveal them, and put them into your hand. Then, shuffle your deck."

Ball Guy's filter (is_ball_item: "Ball" as a WORD, Items only) with a
deck search instead of a hand one.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_ball_item
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="24403c4f-ad37-5412-b551-1850ffd69f3f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ApricornMaker.Name",
    display_name="Apricorn Maker",
    searchable_by=["Apricorn Maker", "Supporter", "ApricornMaker"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_ball_item, count=2, minimum=0, reveal=True,
                          prompt="Choose up to 2 Item cards with Ball in their name."),
)
