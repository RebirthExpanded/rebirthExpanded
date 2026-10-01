"""Neutralization Zone (SV - Shrouded Fable 60/64 -- JP SV6a 063/064).

Stadium, ACE SPEC.

  "Prevent all damage done to Pokemon that don't have a Rule Box (both
   yours and your opponent's) by attacks from your opponent's Pokemon ex
   and Pokemon V.
   This card can't be put into your hand or deck from your discard pile."

Pokemon ex is the Scarlet & Violet "ex" (an XY Pokemon-EX is not one).
The discard-pile clause is the definition flag stays_in_discard: recovery
effects never offer it and the hand/deck moves skip it; an effect that
puts a Stadium into play from the discard pile (Gothitelle's Teleport
Room) still may.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef, has_rule_box, is_pokemon_v, subtypes_for
from spirit.game.session.passives import Passive


class NeutralizationZonePassive(Passive):
    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if calc.target is None or calc.attacker is None:
            return False
        if has_rule_box(calc.target.archetype_id):
            return False
        attacker = calc.attacker.archetype_id
        return "ex" in subtypes_for(attacker) or is_pokemon_v(attacker)


card = StadiumCardDef(
    guid="3d14994b-1dd0-5ccc-8566-38b27d89ad49",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NeutralizationZone.Name",
    display_name="Neutralization Zone",
    searchable_by=["Neutralization Zone", "Stadium", "ACE SPEC", "NeutralizationZone"],
    subtypes=["Stadium", "ACE SPEC"],
    collector_number=60,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Ace,
    passive=NeutralizationZonePassive(),
)
card.stays_in_discard = True
