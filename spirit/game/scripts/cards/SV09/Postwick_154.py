"""Postwick (SV - Journey Together 154/190 -- JP SV9 099/100).

Stadium.

  "Attacks used by Hop's Pokemon (both yours and your opponent's) do 30
   more damage to the opponent's Active Pokemon (before applying Weakness
   and Resistance)."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef, def_for
from spirit.game.session.passives import Passive


def _is_hops(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Hop's ")


class PostwickPassive(Passive):
    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if calc.attacker is not None and _is_hops(calc.attacker):
            calc.amount += 30


card = StadiumCardDef(
    guid="9110a2dc-6586-5308-8cfc-03abb183ae24",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Postwick.Name",
    display_name="Postwick",
    searchable_by=["Postwick", "Stadium", "Postwick"],
    subtypes=["Stadium"],
    collector_number=154,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=PostwickPassive(),
)
