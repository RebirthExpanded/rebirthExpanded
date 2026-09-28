"""Hop's Choice Band (SV - Journey Together 148/190 -- JP SV9 092/100).

Pokemon Tool.

  "Attacks used by the Hop's Pokemon this card is attached to cost [C] less
   and do 30 more damage to your opponent's Active Pokemon (before applying
   Weakness and Resistance)."

[C] less removes one Colorless symbol, like Karate Belt's [F]; an attack
with no Colorless in its cost is not discounted.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef, def_for
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_hops(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Hop's ")


class HopsChoiceBandPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon or not _is_hops(pokemon):
            return cost
        remaining = cost.get("Colorless", 0) - 1
        if remaining > 0:
            cost["Colorless"] = remaining
        elif remaining == 0:
            del cost["Colorless"]
        return cost

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or carrier_pokemon(carrier) is not attacker or not _is_hops(attacker):
            return
        calc.amount += 30


card = PokemonToolCardDef(
    guid="c8307e1c-4a78-5165-b4fa-3a4f11017297",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HopsChoiceBand.Name",
    display_name="Hop's Choice Band",
    searchable_by=["Hop's Choice Band", "Pokémon Tool", "HopsChoiceBand"],
    subtypes=["Pokémon Tool"],
    collector_number=148,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=HopsChoiceBandPassive(),
)
