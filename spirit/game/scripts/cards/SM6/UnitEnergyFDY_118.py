"""Unit Energy FDY (SM - Forbidden Light 118/131 -- JP SM8b 150/150, the art here).

Special Energy.

  "While this card is attached to a Pokemon, this card provides [F][D][Y]
   Energy but provides only 1 Energy at a time.

   While this card is not attached to a Pokemon, it provides [C] Energy."

Unit Energy LPM's shape: the shared multi_type_energy_passive, and a wide
pip crop so the type symbols around the emblem show.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import multi_type_energy_passive
from spirit.game.data_utils import EnergyCardDef

card = EnergyCardDef(
    guid="ea775b3b-30fb-5724-a7d3-8d6ba7a89b25",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.energy.UnitEnergyFDY.Name",
    display_name="Unit Energy FDY",
    searchable_by=["Unit Energy FDY", "Unit Energy FightingDarknessFairy",
                   "Special", "UnitEnergyFDY"],
    subtypes=["Special"],
    collector_number=118,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=multi_type_energy_passive(
        PokemonTypes.FIGHTING, PokemonTypes.DARKNESS, PokemonTypes.FAIRY),
    pip_wide=True,
)
