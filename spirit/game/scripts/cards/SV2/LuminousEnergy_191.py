"""Luminous Energy (SV - Paldea Evolved 191/193 -- JP SV1a 073/073).

Special Energy.  "As long as this card is attached to a Pokemon, it
provides every type of Energy but provides only 1 Energy at a time. If
the Pokemon this card is attached to has any other Special Energy
attached, this card provides [C] Energy instead."
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.effects import is_special_energy
from spirit.game.session.passives import Passive, carrier_pokemon


class LuminousEnergyPassive(Passive):
    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or carrier_pokemon(energy) is not holder:
            return options
        others = [e for e in board.attached_energies(holder)
                  if e is not energy and is_special_energy(e)]
        if others:
            return [[PokemonTypes.COLORLESS.value]]
        return [[option[0].value] for option in ALL_TYPES_ONE_AT_A_TIME]


card = EnergyCardDef(
    guid="186aff6b-0bd6-50ba-980e-00ff0fe12c04",
    key="SV2",
    name="Luminous Energy",
    display_name="Luminous Energy",
    searchable_by=["Luminous Energy", "Special", "LuminousEnergy"],
    subtypes=["Special"],
    collector_number=191,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=LuminousEnergyPassive(),
)
