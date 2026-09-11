"""Cyrus {*} (SM - Ultra Prism 120/156 -- JP SM5S 057/066).

Supporter, Prism Star.

  "You can play this card only if your Active Pokemon is a [W] or [M]
   Pokemon."
  "Your opponent chooses 2 Benched Pokemon and shuffles the others, and all
   cards attached to them, into their deck."

The [W]/[M] clause is a playability condition, so the card is simply not
offered with any other Active. THEY pick the two survivors, so the chooser
opens on their side, and with a Bench of 2 or fewer the card does nothing.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (cyrus_prism_condition,
                                               cyrus_prism_star)
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="8c6260ff-4cde-5666-a92a-da58b55d89d6",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CyrusPrismStar.Name",
    display_name="Cyrus {*}",
    searchable_by=["Cyrus", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=120,
    set_code="SM5",
    rarity=Rarities.Prism,
    effect=cyrus_prism_star,
    condition=cyrus_prism_condition,
)
