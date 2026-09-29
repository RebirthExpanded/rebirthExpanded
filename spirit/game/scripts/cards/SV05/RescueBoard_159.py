"""Rescue Board (SV - Temporal Forces 159/162 -- JP SV5K 064/071).

Pokemon Tool.

  "The Retreat Cost of the Pokemon this card is attached to is [C] less.
   If that Pokemon's remaining HP is 30 or less, it has no Retreat Cost."
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class RescueBoardPassive(Passive):
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        if int(pokemon.get_attribute(AttrID.HP, 0) or 0) <= 30:
            return 0
        return max(0, cost - 1)


card = PokemonToolCardDef(
    guid="4f8d1eb7-e85e-5e04-b405-67d48406f462",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueBoard.Name",
    display_name="Rescue Board",
    searchable_by=["Rescue Board", "Pokémon Tool", "Tool", "RescueBoard"],
    subtypes=["Pokémon Tool", "Tool"],
    collector_number=159,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=RescueBoardPassive(),
)
