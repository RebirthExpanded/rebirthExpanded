"""Plasma Energy (BW - Plasma Storm 127/135 -- JP BW8 051/051, Raiden Knuckle).

Special Energy.  "This card provides [C] Energy."

No text of its own; Team Plasma cards read it by name.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import EnergyCardDef

card = EnergyCardDef(
    guid="6811851b-994c-5d1c-bfe0-b8feaee12cc0",
    key="BW8",
    name="Plasma Energy",
    display_name="Plasma Energy",
    searchable_by=["Plasma Energy", "Special", "PlasmaEnergy"],
    subtypes=["Special"],
    collector_number=127,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
)
