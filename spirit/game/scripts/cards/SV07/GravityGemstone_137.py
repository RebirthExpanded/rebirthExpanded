from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive, carrier_pokemon


class GravityGemstonePassive(Passive):
    """"As long as the Pokemon this card is attached to is in the Active
    Spot, the Retreat Cost of both Active Pokemon is [C] more." Nothing
    changes while the holder sits on the Bench."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if holder is None or not is_in_active_spot(holder):
            return cost
        if pokemon is holder or is_in_active_spot(pokemon):
            return cost + 1
        return cost


card = PokemonToolCardDef(
    guid="13f5798c-8e71-51a3-afdd-a64951e9fdbb",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GravityGemstone.Name",
    display_name="Gravity Gemstone",
    searchable_by=["Gravity Gemstone","Pokémon Tool","Tool","GravityGemstone"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=137,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=GravityGemstonePassive(),
)
