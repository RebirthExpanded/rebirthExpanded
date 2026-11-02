"""Snorlax Doll (SV - Paradox Rift 175/182 -- JP SV4K 059/066). Japanese art.

Item.  "If this card is in your hand when you are setting up to play, you
may put it face down in the Active Spot or on your Bench as if it were a
120-HP Basic Colorless Pokemon. (You can do this only when you are setting
up to play.) At any time during your turn, you may discard this card from
play.

This card can't be affected by any Special Conditions and can't retreat.
If this card is Knocked Out, your opponent can't take any Prize cards for
it."

Lillie's Poke Doll's shape (no Prize, can't retreat) with the fossils'
discard and Rare Fossil's Special Condition immunity. setup_only offers it
as an opening Active or Bench placement -- so a hand whose only "Basic" is
the doll needs no mulligan -- and never as a play from the hand afterwards.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import DollBodyPassive, fossil_discard_ability
from spirit.game.data_utils import FossilItemCardDef

card = FossilItemCardDef(
    guid="a23b3b4f-63e2-56ae-965f-c09361a24d3d",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SnorlaxDoll.Name",
    display_name="Snorlax Doll",
    searchable_by=["Snorlax Doll", "Item", "SnorlaxDoll"],
    subtypes=["Item"],
    collector_number=175,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    setup_only=True,
    passive=DollBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
