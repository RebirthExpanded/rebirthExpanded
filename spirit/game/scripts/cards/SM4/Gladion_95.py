"""Gladion (SM - Crimson Invasion 95/111).

Supporter.

  "Look at your face-down Prize cards and put 1 of them into your hand.
   Then, shuffle this Gladion into your remaining Prize cards and put them
   back face down. If you didn't play this Gladion from your hand, it does
   nothing."

Hisuian Heavy Ball with two knobs turned: any Prize card rather than only
a Basic, and mandatory rather than "you may". The swap into the vacated
slot and the shuffle are identical, so both now go through
ctx.look_at_prizes_take.

Face-down only, like Heavy Ball -- a Prize already turned over by Town Map
is not looked at, not takeable, and not shuffled, so the condition counts
face-down Prizes rather than Prizes.

The last sentence is the anti-copy clause. A Supporter's effect only ever
runs from a hand play in this engine, so there is nothing to gate; it
would matter if something ever replayed a Supporter from another zone.

Like Heavy Ball, this card does NOT go to the discard: it ends up in the
Prize pile, which is why the effect returns whether it was taken and the
Trainer executor leaves it alone.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gladion


def has_face_down_prize(board, player_id, pokemon=None) -> bool:
    area = board.find_player_area(player_id, "prizePile")
    return any(not c.face_up for c in (area.children if area else []))


card = SupporterCardDef(
    guid="b43d09c8-ab22-5d3b-af7f-6f3481608951",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gladion.Name",
    display_name="Gladion",
    searchable_by=["Gladion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    effect=gladion,
    condition=has_face_down_prize,
)
