"""Reversal Energy (SV - Paldea Evolved 192/193).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [C] Energy.
   If you have more Prize cards remaining than your opponent, and if this
   card is attached to an Evolution Pokemon that doesn't have a Rule Box
   (Pokemon ex, Pokemon V, etc. have Rule Boxes), this card provides every
   type of Energy but provides only 3 Energy at a time."

Neo Upper Energy's shape with a harder gate. Neo Upper asks one question
of the holder (is it a Stage 2); this asks three, and one of them is not
about the holder at all:

  * you are BEHIND -- more Prizes still on your side than on theirs, so it
    switches on as you lose and switches off again the moment you catch up;
  * the holder is an Evolution;
  * the holder has no Rule Box.

Unlike Triple Acceleration Energy it is not restricted to Evolution
Pokemon -- it goes on anything and simply pays 1 there, so no attach_to
and no discard_if_invalid. All three conditions live in the passive, which
is re-read on every cost check, so the Energy strengthens and weakens with
the prize count on its own.

max_energy_provided = 3 is the pip's ceiling, not a gameplay figure: the
attachment pip names the card, so one that can act as three Energy is
cropped to the three emblems its art prints.
"""

from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.card_effects.support_common import (
    more_prizes_remaining_than_opponent,
)
from spirit.game.data_utils import EnergyCardDef, has_rule_box
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.session.effects import is_evolution_pokemon
from spirit.game.session.passives import Passive, carrier_pokemon

ALL_TYPES_THREE_AT_A_TIME = [
    [option[0].value] * 3 for option in ALL_TYPES_ONE_AT_A_TIME
]


class ReversalEnergyPassive(Passive):
    """Behind on Prizes, on a Rule Box-less Evolution: every type, 3 at a
    time. Otherwise the printed single Colorless."""

    max_energy_provided = 3   # pip shows the three emblems on the art

    def modify_energy_provided(self, options, energy, holder, board):
        if carrier_pokemon(energy) is not holder or holder is None:
            return options
        if not is_evolution_pokemon(holder) or has_rule_box(holder.archetype_id):
            return options
        owner = energy.owning_player_id or holder.owning_player_id
        if owner is None or not more_prizes_remaining_than_opponent(board, owner):
            return options
        return [list(option) for option in ALL_TYPES_THREE_AT_A_TIME]


card = EnergyCardDef(
    guid="61b7bdfa-01c8-5ee4-9b0c-eb8a7032dccf",
    key="SV2",
    name="Reversal Energy",
    display_name="Reversal Energy",
    searchable_by=["Reversal Energy", "Special", "ReversalEnergy"],
    subtypes=["Special"],
    collector_number=192,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=ReversalEnergyPassive(),
)
