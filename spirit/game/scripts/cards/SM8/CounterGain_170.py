"""Counter Gain (SM - Lost Thunder 170/214 -- JP SM-P deck build box 015).

Pokemon Tool.

  "If you have more Prize cards remaining than your opponent, the attacks
   of the Pokemon this card is attached to cost [C] less."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import more_prizes_remaining_than_opponent
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class CounterGainPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon or "Colorless" not in cost:
            return cost
        if not more_prizes_remaining_than_opponent(board, pokemon.owning_player_id):
            return cost
        remaining = cost["Colorless"] - 1
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


card = PokemonToolCardDef(
    guid="edb44542-b7f8-5848-9e90-e83855472c90",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterGain.Name",
    display_name="Counter Gain",
    searchable_by=["Counter Gain", "Pokémon Tool", "CounterGain"],
    subtypes=["Pokémon Tool"],
    collector_number=170,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    passive=CounterGainPassive(),
)
