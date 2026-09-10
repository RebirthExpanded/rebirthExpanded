"""Counter Energy (SM - Crimson Invasion 100/111).

Special Energy.

  "This card provides [C] Energy. If you have more Prize cards remaining
   than your opponent, and if this card is attached to a Pokemon that isn't
   a Pokemon-GX or Pokemon-EX, this card provides every type of Energy but
   provides only 2 Energy at a time."

Reversal Energy's ancestor: the same "switch on while you are behind"
shape, two Energy instead of three, and a different exclusion -- Reversal
asks for an Evolution with no Rule Box, this one only that the holder is
not a GX or an EX.

That exclusion is the uppercase SM/XY mechanics alone, the way Wally's is:
"Pokemon-EX" and the SV-era "Pokemon ex" are separate things, and a card
printed in 2017 naming the first does not reach the second. So Counter
Energy still turns on for a Pokemon ex. Say the word if this pool would
rather read it the other way.

Both conditions live in the passive, re-read on every cost check, so it
strengthens and weakens with the Prize count without being re-attached.
max_energy_provided = 2 is the pip's ceiling: the attachment pip has to
name the card, so one that can act as two Energy shows both emblems.
"""

from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.card_effects.support_common import (
    more_prizes_remaining_than_opponent,
)
from spirit.game.data_utils import EnergyCardDef, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon

ALL_TYPES_TWO_AT_A_TIME = [
    [option[0].value] * 2 for option in ALL_TYPES_ONE_AT_A_TIME
]


def _is_gx_or_uppercase_ex(pokemon) -> bool:
    """Pokemon-GX and the uppercase XY-era Pokemon-EX; see the module note."""
    return any(s in ("GX", "EX") for s in subtypes_for(pokemon.archetype_id))


class CounterEnergyPassive(Passive):
    """Ahead on Prizes remaining, on a Pokemon that is neither GX nor EX:
    every type, 2 at a time. Otherwise the printed single Colorless."""

    max_energy_provided = 2   # pip shows both emblems on the art

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or carrier_pokemon(energy) is not holder:
            return options
        if _is_gx_or_uppercase_ex(holder):
            return options
        owner = energy.owning_player_id or holder.owning_player_id
        if owner is None or not more_prizes_remaining_than_opponent(board, owner):
            return options
        return [list(option) for option in ALL_TYPES_TWO_AT_A_TIME]


card = EnergyCardDef(
    guid="cfbbdc75-143f-57d5-b31e-1133dc2a446c",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.energy.CounterEnergy.Name",
    display_name="Counter Energy",
    searchable_by=["Counter Energy", "Special", "CounterEnergy"],
    subtypes=["Special"],
    collector_number=100,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=CounterEnergyPassive(),
)
