"""Assault Vest (XY - BREAKthrough 133/162 -- JP XY9-R 055/059).

Pokemon Tool.

  "Any damage done to the Pokemon this card is attached to by attacks from
   your opponent's Pokemon that have any Special Energy attached to them
   is reduced by 40 (after applying Weakness and Resistance)."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.effects import is_special_energy
from spirit.game.session.passives import Passive, carrier_pokemon


class AssaultVestPassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing) or calc.attacker is None:
            return
        if calc.target is not carrier_pokemon(carrier):
            return
        if any(is_special_energy(e) for e in calc.board.attached_energies(calc.attacker)):
            calc.amount = max(0, calc.amount - 40)


card = PokemonToolCardDef(
    guid="31206fb2-228e-5eaa-bc67-37b6e9274b8e",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AssaultVest.Name",
    display_name="Assault Vest",
    searchable_by=["Assault Vest", "Pokémon Tool", "AssaultVest"],
    subtypes=["Pokémon Tool"],
    collector_number=133,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=AssaultVestPassive(),
)
