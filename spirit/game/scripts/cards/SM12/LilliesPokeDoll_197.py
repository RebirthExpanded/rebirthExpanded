"""Lillie's Poke Doll (SM - Cosmic Eclipse 197/236 -- JP SM11b 043/049).

Item.

  "Play this card as if it were a 30-HP Colorless Basic Pokemon. At any
   time during your turn (before your attack), if this Pokemon is your
   Active Pokemon, you may discard all cards from it and put it on the
   bottom of your deck.

   This card can't retreat. If this card is Knocked Out, your opponent
   can't take any Prize cards for it."

A fossil in every structural sense, so it is a FossilItemCardDef: the
archetype stays a Trainer-Item, which is what makes it behave the way the
card reads on both of the points that matter here. In hand it is an Item,
so an Item lock stops it being put down and a deck search for a Basic
Pokemon (Nest Ball, Quick Ball) cannot find it. On the Bench it is a Basic
Pokemon, so anything reading the board -- Risky Ruins, Silent Lab, a spread
attack -- sees one.

Two rules-text lines beyond the fossils: it cannot retreat (which the
fossils share) and knocking it out is worth NO Prize card, which is a flat
zero rather than a subtraction -- an effect that would otherwise add one is
adding to nothing.

Its own exit is not the fossils' discard: it goes to the BOTTOM OF THE
DECK, only from the Active spot, and everything attached is discarded on
the way. Emptying the Active spot promotes a new Active, so the ability
defers that like the fossil discard does.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (DollBodyPassive,
                                               doll_bottom_of_deck_ability)
from spirit.game.data_utils import FossilItemCardDef

card = FossilItemCardDef(
    guid="632fb2d5-3872-595a-a229-7822a5781d80",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesPokeDoll.Name",
    display_name="Lillie's Poké Doll",
    searchable_by=["Lillie's Poké Doll", "Lillie's Poke Doll", "Item",
                   "LilliesPokeDoll"],
    subtypes=["Item"],
    collector_number=197,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=30,
    passive=DollBodyPassive(),
    abilities=[doll_bottom_of_deck_ability()],
)
