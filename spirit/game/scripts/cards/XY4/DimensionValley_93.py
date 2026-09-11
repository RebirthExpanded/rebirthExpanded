"""Dimension Valley (XY - Phantom Forces 93/119 -- JP XY4 077/088).

Stadium.

  "Each [P] Pokemon's attacks (both yours and your opponent's) cost [C]
   less."

Thunder Mountain's discount on the Colorless half of a cost: one [C] off
any Psychic Pokemon's attack, on either side; an attack with no [C] in
its cost is unchanged.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import StadiumCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.session.passives import Passive


class DimensionValleyPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if not is_pokemon_of_type(pokemon, PokemonTypes.PSYCHIC):
            return cost
        remaining = cost.get("Colorless", 0) - 1
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            cost.pop("Colorless", None)
        return cost


card = StadiumCardDef(
    passive=DimensionValleyPassive(),
    guid="8853f0dd-52d8-574f-a2f6-0e3314bc9feb",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DimensionValley.Name",
    display_name="Dimension Valley",
    searchable_by=["Dimension Valley", "Stadium", "DimensionValley"],
    subtypes=["Stadium"],
    collector_number=93,
    set_code="XY4",
    rarity=Rarities.Uncommon,
)
