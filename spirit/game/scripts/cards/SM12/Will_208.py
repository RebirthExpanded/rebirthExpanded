"""Will (SM - Cosmic Eclipse 208/236 -- JP SM11b 052/049).

Supporter.

  "The next time you flip any number of coins for the effect of an attack, Ability, or Trainer card this turn, choose heads or tails for the first coin flip."

The choice is made when Will is played and parked on the turn state;
the first flip this player makes afterwards -- one coin, several, or a
"flip until tails" run -- has its first coin replaced and the choice is
spent. It lapses at the end of the turn unused.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import will
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="a2848939-917d-5827-a80b-638f9b768f29",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Will.Name",
    display_name="Will",
    searchable_by=["Will", "Supporter", "Will"],
    subtypes=["Supporter"],
    collector_number=208,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=will,
    condition=None,
)
