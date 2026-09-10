"""Memory Energy (SM - Lost Thunder 194/214).

Special Energy.

  "This card provides [C] Energy."
  "The Pokemon this card is attached to can use any attack from its
   previous Evolutions. (You still need the necessary Energy to use each
   attack.)"

The previous Evolutions are the cards tucked under the holder in its own
stack, so the passive walks them and hands their Attacks back through
granted_attacks -- the hook Ditto's Sudden Transformation already uses.
Nothing is copied or rewritten: the Attack objects are the pre-evolution
cards' own, so their costs, their damage and their effects apply as
printed, and the reminder text about Energy takes care of itself.

Only the Pokemon this card is attached to gains them; the pip is a plain
Colorless one.
"""

from spirit.game.data_utils import EnergyCardDef, PokemonTypes
from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import pre_evolution_attacks
from spirit.game.session.passives import Passive, carrier_pokemon


class MemoryEnergyPassive(Passive):
    """The holder may use the attacks printed on what it evolved from.

    Shining Celebi and Relicanth say the same thing for a whole side; the
    walk of the stack is shared with them (pre_evolution_attacks).
    """

    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        return pre_evolution_attacks(pokemon)


card = EnergyCardDef(
    guid="bbc960f6-0f69-5b5d-8387-e1078773f849",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.energy.MemoryEnergy.Name",
    display_name="Memory Energy",
    searchable_by=["Memory Energy", "Special", "MemoryEnergy"],
    subtypes=["Special"],
    collector_number=194,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=MemoryEnergyPassive(),
)
