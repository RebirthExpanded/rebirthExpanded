"""Wait and See Hammer (SM - Lost Thunder 192/214 -- JP SM8 087/095).

Item.

  "You can use this card only if you go second, and only on your first turn. Discard an Energy from 1 of your opponent's Pokémon."

"Only if you go second, and only on your first turn" is turn 2 of the
game, the reading Shaymin (ASR 14) and Scatterbug (FLI 5) take. Any of
their Pokemon, Bench included, and only one with an Energy to lose is
offered.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (wait_and_see_hammer,
                                               wait_and_see_hammer_condition)
from spirit.game.data_utils import ItemCardDef

card = ItemCardDef(
    guid="4cabf44e-0568-51a3-9279-fd184f203274",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WaitandSeeHammer.Name",
    display_name="Wait and See Hammer",
    searchable_by=["Wait and See Hammer", "Item", "WaitandSeeHammer"],
    subtypes=["Item"],
    collector_number=192,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=wait_and_see_hammer,
    condition=wait_and_see_hammer_condition,
)
