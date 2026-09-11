"""Beast Ball (SM - Celestial Storm 125/168 -- JP SM-P 236/SM-P).

Item.

  "Look at your face-down Prize cards. You may reveal an Ultra Beast card
   you find there, put it into your hand, and put this Beast Ball in its
   place. (If you don't reveal an Ultra Beast card, put this card in the
   discard pile.) Then, shuffle your face-down Prize cards."

The Japanese name is ウルトラボール, which is NOT the Ultra Ball of this pool
-- that is ハイパーボール. This is the Ultra Beast's ball, and the two are
different cards.

Mechanically it is Hisuian Heavy Ball with the filter changed from "a Basic
Pokemon" to "an Ultra Beast", so it goes through the same
look_at_prizes_take: take the card, drop this one face down into the slot it
vacated, shuffle the face-down Prizes. Decline and this card is discarded
the ordinary way instead.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import beast_ball, has_face_down_prize
from spirit.game.data_utils import ItemCardDef

card = ItemCardDef(
    guid="7b92b827-7f31-58a0-96f1-a3d18210d505",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastBall.Name",
    display_name="Beast Ball",
    searchable_by=["Beast Ball", "Item", "BeastBall"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=beast_ball,
    condition=has_face_down_prize,
)
