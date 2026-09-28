"""Unit Energy GRW (SM - Ultra Prism 137/156 -- JP SM5S 066/066).

Special Energy.

  "While this card is attached to a Pokemon, this card provides [G][R][W]
   Energy but provides only 1 Energy at a time.

   While this card is not attached to a Pokemon, it provides [C] Energy."

Unit Energy LPM's shape: the shared multi_type_energy_passive, and a wide
pip crop so the type symbols around the emblem show.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import multi_type_energy_passive
from spirit.game.data_utils import EnergyCardDef

card = EnergyCardDef(
    guid="86763438-9ccc-5627-acd8-e9ec0906ff08",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.energy.UnitEnergyGRW.Name",
    display_name="Unit Energy GRW",
    searchable_by=["Unit Energy GRW", "Unit Energy GrassFireWater",
                   "Special", "UnitEnergyGRW"],
    subtypes=["Special"],
    collector_number=137,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=multi_type_energy_passive(
        PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER),
    pip_wide=True,
)
