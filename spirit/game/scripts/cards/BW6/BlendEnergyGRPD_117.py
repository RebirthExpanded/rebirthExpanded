"""Blend Energy GRPD (BW - Dragons Exalted 117/124 -- JP BW5 050/050).

Special Energy.

  "This card provides [C] Energy. While this card is attached to a Pokemon,
   this card provides [G][R][P][D] Energy but provides only 1 Energy at a
   time."

Blend Energy WLFM's sibling: the shared multi_type_energy_passive and a
wide pip crop.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import multi_type_energy_passive
from spirit.game.data_utils import EnergyCardDef

card = EnergyCardDef(
    guid="80c97433-1ec5-50ca-8a42-25d26eb8ec09",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.energy.BlendEnergyGRPD.Name",
    display_name="Blend Energy GRPD",
    searchable_by=["Blend Energy GRPD",
                   "Blend Energy GrassFirePsychicDarkness",
                   "Special", "BlendEnergyGRPD"],
    subtypes=["Special"],
    collector_number=117,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=multi_type_energy_passive(
        PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.PSYCHIC,
        PokemonTypes.DARKNESS),
    pip_wide=True,
)
