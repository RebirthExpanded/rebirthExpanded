"""Twin Energy (SWSH - Rebel Clash 174/192).

Special Energy.

  "As long as this card is attached to a Pokemon that isn't a Pokemon V or
   a Pokemon-GX, it provides [C][C] Energy."
  "If this card is attached to a Pokemon V or a Pokemon-GX, it provides [C]
   Energy instead."

The printed two Colorless stand everywhere except on a Pokemon V / GX,
where the passive narrows the card to a single Colorless.
"""

from spirit.game.data_utils import EnergyCardDef, is_pokemon_v, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class TwinEnergyPassive(Passive):
    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or carrier_pokemon(energy) is not holder:
            return options
        if is_pokemon_v(holder.archetype_id) or "GX" in subtypes_for(holder.archetype_id):
            return [[PokemonTypes.COLORLESS.value]]
        return options


card = EnergyCardDef(
    guid="616713d7-e9f3-5aea-8ae5-7072c779b3e9",
    key="SWSH2",
    name="Twin Energy",
    display_name="Twin Energy",
    searchable_by=["Twin Energy", "Special"],
    subtypes=["Special"],
    collector_number=174,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
    passive=TwinEnergyPassive(),
)
