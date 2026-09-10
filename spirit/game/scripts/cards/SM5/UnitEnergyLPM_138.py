"""Unit Energy LPM (SM - Ultra Prism 138/156 -- JP SM5M 066/066).

Special Energy.

  "While this card is attached to a Pokemon, this card provides [L][P][M]
   Energy but provides only 1 Energy at a time.

   While this card is not attached to a Pokemon, it provides [C] Energy."

Three types, one at a time -- the same shape as Blend Energy WLFM with a
shorter list, so both sit on the shared multi_type_energy_passive.

The pip that shows on the Pokemon it is attached to prints the types
rather than a single star: the pip crop is widened for these two through
pip_wide, because their art puts the type symbols AROUND the emblem and a
tight crop on the ball says nothing about what the card provides.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import multi_type_energy_passive
from spirit.game.data_utils import EnergyCardDef

card = EnergyCardDef(
    guid="187488d6-a5d1-537c-8c8b-12c7fa39a30c",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.energy.UnitEnergyLPM.Name",
    display_name="Unit Energy LPM",
    searchable_by=["Unit Energy LPM", "Unit Energy LightningPsychicMetal",
                   "Special", "UnitEnergyLPM"],
    subtypes=["Special"],
    collector_number=138,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=multi_type_energy_passive(
        PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.METAL),
    pip_wide=True,
)
