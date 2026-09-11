"""Wondrous Labyrinth {*} (SM - Team Up 158/181 -- JP SM8b 143/150).

Stadium, Prism Star.

  "The attacks of non-[Y] Pokemon (both yours and your opponent's) cost [C]
   more."
  "Whenever any player plays an Item or Supporter card from their hand,
   prevent all effects of that card done to this Stadium card."

Thunder Mountain {*} with the sign flipped: the same ShieldedStadiumPassive,
and a modify_attack_cost that ADDS [C] rather than removing an [L]. The tax
is on the Pokemon's TYPE, not its owner -- a Fairy Pokemon pays nothing on
either side of the table, everything else pays.

Prism Star brings its own rules and needs nothing here: the deck cap lives
in game/rules.py and discard_area_name already sends this card to the Lost
Zone whenever it would be discarded, the Stadium it replaces included.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import WondrousLabyrinthPassive
from spirit.game.data_utils import StadiumCardDef

card = StadiumCardDef(
    passive=WondrousLabyrinthPassive(),
    guid="88b4fba2-bd05-5a01-9efb-70ddc0266ef6",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WondrousLabyrinthPrismStar.Name",
    display_name="Wondrous Labyrinth {*}",
    searchable_by=["Wondrous Labyrinth", "Stadium", "Prism Star",
                   "WondrousLabyrinth"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=158,
    set_code="SM9",
    rarity=Rarities.Prism,
)
