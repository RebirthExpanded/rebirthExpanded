"""Robo Substitute Team Flare Gear (XY - Phantom Forces 102/119 --
JP XY 119/171).

Item.

  "Play this card as if it were a 30 HP Colorless Basic Pokemon. At any
   time during your turn (before your attack), you may discard this card
   from play.

   This card can't retreat. If this card is Knocked Out, your opponent
   can't take any Prize Cards for it."

Lillie's Poke Doll's older sibling and the same shape: an Item in hand (so
an Item lock stops it and no Basic-Pokemon search can find it), a 30-HP
Colorless Basic on the board, no retreat, and no Prize for whoever knocks
it out.

The difference is the exit. This one simply discards itself, from
anywhere in play rather than only the Active spot, which is exactly the
fossils' Discard ability -- so it reuses that one unchanged.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (DollBodyPassive,
                                               fossil_discard_ability)
from spirit.game.data_utils import FossilItemCardDef

card = FossilItemCardDef(
    guid="18f49d37-3f32-5b8e-9af3-2938c94beb27",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoboSubstitute.Name",
    display_name="Robo Substitute Team Flare Gear",
    searchable_by=["Robo Substitute Team Flare Gear", "Robo Substitute",
                   "Item", "RoboSubstitute"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=30,
    passive=DollBodyPassive(),
    abilities=[fossil_discard_ability()],
)
