"""Mystery Energy (XY - Phantom Forces 112/119 -- JP XY4 088/088, the art here).

Special Energy.

  "This card can only be attached to a [P] Pokemon. This card provides
   [P] Energy only while this card is attached to a [P] Pokemon."
  "The Retreat Cost of the [P] Pokemon this card is attached to is [C][C]
   less."
  "(If this card is attached to anything other than a [P] Pokemon,
   discard this card.)"

Flash Energy's shape: attach_to + discard_if_invalid keep it on Psychic
Pokemon only, so the "provides only while" clause never has a case to
answer; the retreat discount rides the holder.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import retreat_discount
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.effects import is_pokemon_of_type


def _psychic_pokemon(pokemon) -> bool:
    return is_pokemon_of_type(pokemon, PokemonTypes.PSYCHIC)


card = EnergyCardDef(
    guid="50d2a99d-2b2b-52eb-a90d-d31d51b90fe8",
    key="XY4",
    name="Mystery Energy",
    display_name="Mystery Energy",
    searchable_by=["Mystery Energy", "Special", "MysteryEnergy"],
    subtypes=["Special"],
    collector_number=112,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=True,
    attach_to=_psychic_pokemon,
    discard_if_invalid=True,
    provides=[[PokemonTypes.PSYCHIC]],
    passive=retreat_discount(2),
)
