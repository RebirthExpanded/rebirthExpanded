"""Big Air Balloon (SV035 155 -- JP SV2a 158; English MEW/155). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.session.effects import is_stage2_pokemon
from spirit.game.session.passives import carrier_pokemon


class BigAirBalloonPassive(Passive):
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        return 0 if pokemon is carrier_pokemon(carrier) and is_stage2_pokemon(pokemon) else cost


card = PokemonToolCardDef(
    guid="c705e9a8-8a78-5728-b392-e9427fb2af2b",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BigAirBalloon.Name",
    display_name="Big Air Balloon",
    searchable_by=["Big Air Balloon", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=155,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    passive=BigAirBalloonPassive(),
)
