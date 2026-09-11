"""Recycle Energy (SM - Unified Minds 212/236 -- JP SM10b 050/054).

Special Energy.

  "This card provides [C] Energy. If this card would be discarded from
   play, put it into your hand instead."

U-Turn Board's discard_destination on an Energy: discarded while attached
(retreat, an attack cost, Crushing Hammer, its Pokemon being Knocked Out)
it goes to its owner's hand; discarded out of the hand or milled from the
deck it is not "from play" and goes to the discard pile.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.passives import Passive


class RecycleEnergyPassive(Passive):
    def discard_destination(self, card, carrier):
        return "hand" if card is carrier else None


card = EnergyCardDef(
    guid="7d906f9e-e0df-53c6-abf1-40b92f9aae5d",
    key="SM11",
    name="Recycle Energy",
    display_name="Recycle Energy",
    searchable_by=["Recycle Energy", "Special", "RecycleEnergy"],
    subtypes=["Special"],
    collector_number=212,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=RecycleEnergyPassive(),
)
