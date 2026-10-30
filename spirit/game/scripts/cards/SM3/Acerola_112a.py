"""Acerola (SM - Burning Shadows 112/147 -- JP SMN 043/060).

Supporter.

  "Put 1 of your Pokemon that has any damage counters on it and all cards
   attached to it into your hand."

Everything comes back: the Pokemon, its Energy, its Tool and any tucked
pre-evolutions, all as separate cards in hand. Damage counters are not
cards -- they simply stop existing when the Pokemon leaves play, which is
the point of the card.

Playable only with something damaged on your board, so that is a condition
rather than a mid-effect check.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import acerola, acerola_condition
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="14a0b888-bb49-5ec2-82c4-42948c835eb5",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Acerola.Name",
    display_name="Acerola",
    searchable_by=["Acerola", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=acerola,
    condition=acerola_condition,
)
