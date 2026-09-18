"""Flash Energy (XY - Ancient Origins 83/98 -- JP XY7-B 080/081, the art
here).

Special Energy.

  "This card can only be attached to a [L] Pokemon. This card provides
   [L] Energy only while this card is attached to a [L] Pokemon. The [L]
   Pokemon this card is attached to has no Weakness. (If this card is
   attached to anything other than a [L] Pokemon, discard this card.)"

Rapid Strike Energy's shape: attach_to restricts the hand attach,
discard_if_invalid sweeps it off a non-[L] holder (a holder that stops
being [L] included), and the no-Weakness passive answers only for a [L]
holder.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import no_weakness_passive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.session.passives import carrier_pokemon


def _lightning_pokemon(pokemon) -> bool:
    return is_pokemon_of_type(pokemon, PokemonTypes.LIGHTNING)


def _lightning_holder(target, carrier) -> bool:
    holder = carrier_pokemon(carrier)
    return holder is target and _lightning_pokemon(target)


card = EnergyCardDef(
    guid="bfb7f6e7-a318-580f-8f15-64a6ee39c5c3",
    key="XY7",
    name="Flash Energy",
    display_name="Flash Energy",
    searchable_by=["Flash Energy", "Special", "FlashEnergy"],
    subtypes=["Special"],
    collector_number=83,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=True,
    attach_to=_lightning_pokemon,
    discard_if_invalid=True,
    provides=[[PokemonTypes.LIGHTNING]],
    passive=no_weakness_passive(protects=_lightning_holder),
)
