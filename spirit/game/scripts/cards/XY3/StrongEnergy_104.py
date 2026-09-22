"""Strong Energy (XY - Furious Fists 104/111 -- JP XY3 096/096, the art here).

Special Energy.

  "This card can only be attached to [F] Pokemon. This card provides [F]
   Energy only while this card is attached to a [F] Pokemon."
  "The attacks of the [F] Pokemon this card is attached to do 20 more
   damage to your opponent's Active Pokemon (before applying Weakness
   and Resistance)."
  "(If this card is attached to anything other than a [F] Pokemon,
   discard this card.)"

Flash Energy's type gate with Muscle Band's boost: the holder must be
Fighting for either half, which attach_to + discard_if_invalid already
guarantee.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import typed_damage_boost_tool
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.effects import is_pokemon_of_type

BOOST = 20


def _fighting_pokemon(pokemon) -> bool:
    return is_pokemon_of_type(pokemon, PokemonTypes.FIGHTING)


card = EnergyCardDef(
    guid="5ee25447-0c42-54df-b22e-d0d75ccfcc5d",
    key="XY3",
    name="Strong Energy",
    display_name="Strong Energy",
    searchable_by=["Strong Energy", "Special", "StrongEnergy"],
    subtypes=["Special"],
    collector_number=104,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.FIGHTING,
    is_special=True,
    attach_to=_fighting_pokemon,
    discard_if_invalid=True,
    provides=[[PokemonTypes.FIGHTING]],
    passive=typed_damage_boost_tool(lambda target: True, BOOST, to_active_only=True),
)
