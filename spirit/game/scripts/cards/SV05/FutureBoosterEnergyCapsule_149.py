"""Future Booster Energy Capsule (SV - Temporal Forces 149/162 -- JP SV5M
065/071).

Pokemon Tool.  "The Future Pokemon this card is attached to has no Retreat
Cost, and the attacks it uses do 20 more damage to your opponent's Active
Pokemon (before applying Weakness and Resistance)."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef, subtypes_for
from spirit.game.session.passives import Passive, carrier_pokemon


def _future(pokemon) -> bool:
    return "Future" in subtypes_for(pokemon.archetype_id)


class FutureBoosterPassive(Passive):
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        return 0 if holder is pokemon and _future(holder) else cost

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if calc.is_attack and calc.is_opposing and calc.to_active \
                and holder is calc.attacker and _future(holder):
            calc.amount += 20


card = PokemonToolCardDef(
    guid="34a3aed7-b451-5c41-afe8-6d223b276326",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FutureBoosterEnergyCapsule.Name",
    display_name="Future Booster Energy Capsule",
    searchable_by=["Future Booster Energy Capsule", "Pokémon Tool", "FutureBoosterEnergyCapsule"],
    subtypes=["Pokémon Tool"],
    collector_number=149,
    set_code="SV05",
    rarity=Rarities.Uncommon,
    regulation_mark="H",
    passive=FutureBoosterPassive(),
)
