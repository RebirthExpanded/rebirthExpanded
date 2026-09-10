"""Blend Energy WLFM (BW - Dragons Exalted 118/124 -- JP BW5 050/050).

Special Energy.

  "This card provides [C] Energy. While this card is attached to a Pokemon,
   this card provides [W][L][F][M] Energy but provides only 1 Energy at a
   time."

Unit Energy LPM with a fourth type, and the same shared passive. Off a
Pokemon it is the printed Colorless, which is what matters for the cards
that count Energy in a hand or a discard pile.

Its pip is widened the same way (pip_wide): the art rings the emblem with
the four type symbols, and the attachment pip should say which four.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import multi_type_energy_passive
from spirit.game.data_utils import EnergyCardDef

card = EnergyCardDef(
    guid="c722b208-65c1-5ee3-ae15-6c2697331348",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.energy.BlendEnergyWLFM.Name",
    display_name="Blend Energy WLFM",
    searchable_by=["Blend Energy WLFM",
                   "Blend Energy WaterLightningFightingMetal",
                   "Special", "BlendEnergyWLFM"],
    subtypes=["Special"],
    collector_number=118,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=multi_type_energy_passive(
        PokemonTypes.WATER, PokemonTypes.LIGHTNING, PokemonTypes.FIGHTING,
        PokemonTypes.METAL),
    pip_wide=True,
)
