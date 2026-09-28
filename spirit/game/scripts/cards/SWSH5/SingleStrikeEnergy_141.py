"""Single Strike Energy (SWSH - Battle Styles 141/163).

Special Energy.

  "This card can only be attached to a Single Strike Pokemon. If this card
   is attached to anything other than a Single Strike Pokemon, discard this
   card."
  "As long as this card is attached to a Pokemon, it provides [F] and [D]
   Energy but provides only 1 Energy at a time, and the attacks of the
   Pokemon this card is attached to do 20 more damage to your opponent's
   Active Pokemon (before applying Weakness and Resistance)."

Rapid Strike Energy's restriction shape (attach_to + discard_if_invalid)
with two one-at-a-time options, and the Gloves damage boost with no type
filter -- the passive already reads only the holder's attacks against the
opposing Active, before Weakness and Resistance.
"""

from spirit.game.data_utils import EnergyCardDef, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import typed_damage_boost_tool


def is_single_strike(pokemon) -> bool:
    return "Single Strike" in subtypes_for(pokemon.archetype_id)


card = EnergyCardDef(
    guid="29bb9bbb-02ca-5e9a-8dc4-6b8ec78bbc53",
    key="SWSH5",
    name="Single Strike Energy",
    display_name="Single Strike Energy",
    searchable_by=["Single Strike Energy", "Special", "Single Strike"],
    subtypes=["Special", "Single Strike"],
    collector_number=141,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=is_single_strike,
    discard_if_invalid=True,
    provides=[[PokemonTypes.FIGHTING], [PokemonTypes.DARKNESS]],
    passive=typed_damage_boost_tool(lambda target: True, 20),
)
