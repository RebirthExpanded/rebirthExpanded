"""Archie's Ace in the Hole (XY - Primal Clash 124/160 -- JP XY5-Bt 045/070).

Supporter.

  "You can play this card only when it is the last card in your hand. Put a Water Pokémon from your discard pile onto your Bench. Then, draw 5 cards."

Three gates, all up front: this is the only card in hand, a [W]
Pokemon sits in the discard, and the Bench has room. ANY [W] Pokemon --
an evolved one lands on the Bench as it is, which is the whole trick.
Its Team Magma twin, Maxie's Hidden Ball Trick, is Expanded-banned; this
one is not.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (archies_ace_condition,
                                               archies_ace_in_the_hole)
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="cca35cc0-84fc-505c-a460-8e32657578a4",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArchiesAceintheHole.Name",
    display_name="Archie's Ace in the Hole",
    searchable_by=["Archie's Ace in the Hole", "Supporter", "ArchiesAceintheHole"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=archies_ace_in_the_hole,
    condition=archies_ace_condition,
)
