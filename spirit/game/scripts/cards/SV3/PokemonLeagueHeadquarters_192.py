"""Pokémon League Headquarters (SV3 192 -- JP SV3 108; English OBF/192). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.session.effects import is_basic_pokemon_in_play


class LeagueHQPassive(Passive):
    """Attacks used by Basic Pokemon cost [C] more."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if is_basic_pokemon_in_play(pokemon):
            cost = dict(cost)
            cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


card = StadiumCardDef(
    guid="489da875-11ed-542d-b15a-b5e444b39c4c",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonLeagueHeadquarters.Name",
    display_name="Pokémon League Headquarters",
    searchable_by=["Pokémon League Headquarters", "Stadium"],
    subtypes=["Stadium"],
    collector_number=192,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    passive=LeagueHQPassive(),
)
