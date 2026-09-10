"""Roller Skates (XY 125/146 -- JP XY1 056/060).

Item.

  "Flip a coin. If heads, draw 3 cards."

The coin decides everything, so tails costs the card and nothing else.
No deck gate: an Item that draws is playable with an empty deck the same
way any draw effect is -- drawing from nothing simply draws nothing, and
the deck-out check belongs to the start of a turn.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.data_utils import ItemCardDef

card = ItemCardDef(
    guid="17906c4d-54ce-5bc2-b397-d55588b295d5",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RollerSkates.Name",
    display_name="Roller Skates",
    searchable_by=["Roller Skates", "Item", "RollerSkates"],
    subtypes=["Item"],
    collector_number=125,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=flip_or_nothing(then=draw_attack(3)),
)
