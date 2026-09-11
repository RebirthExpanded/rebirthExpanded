"""Metal Energy (JP XY Hyper Metal Chain Deck 60 -- unnumbered basic
Energy; HMC 19 is a pool-local slot)."""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import EnergyCardDef

card = EnergyCardDef(
    guid="4199b965-d0a7-5bb9-98fb-ee7869fa6717",
    key="HMC",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="HMC",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.METAL,
    is_special=False,
)
