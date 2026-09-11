"""Karate Belt (SM - Unified Minds 201/236 -- JP SM10a 049/054).

Pokemon Tool.

  "If you have more Prize cards remaining than your opponent, the attacks
   of the Pokemon this card is attached to cost [F] less."

[F] less is one Fighting symbol, not one Energy of any kind: an attack with
no [F] in its cost is not discounted.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import more_prizes_remaining_than_opponent
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class KarateBeltPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        if not more_prizes_remaining_than_opponent(board, pokemon.owning_player_id):
            return cost
        if "Fighting" not in cost:
            return cost
        remaining = cost["Fighting"] - 1
        if remaining > 0:
            cost["Fighting"] = remaining
        else:
            del cost["Fighting"]
        return cost


card = PokemonToolCardDef(
    guid="3cb1f99a-6a32-5ca6-9f5d-5db1487e9c95",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KarateBelt.Name",
    display_name="Karate Belt",
    searchable_by=["Karate Belt", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=201,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    passive=KarateBeltPassive(),
)
