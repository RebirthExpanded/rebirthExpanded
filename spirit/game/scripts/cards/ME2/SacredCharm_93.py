"""Sacred Charm (ME - Phantasmal Flames 93 -- JP M2 075/080).

Pokemon Tool.

  "The Pokemon this card is attached to takes 30 less damage from attacks
   from your opponent's Pokemon that have an Ability (after applying
   Weakness and Resistance)."

"Has an Ability" is the printed Ability (Chimecho's reading): an Ability
lock doesn't unprint it.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import has_printed_ability
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class SacredCharmPassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing) or calc.attacker is None:
            return
        if carrier_pokemon(carrier) is not calc.target:
            return
        if has_printed_ability(calc.attacker):
            calc.amount = max(0, calc.amount - 30)


card = PokemonToolCardDef(
    guid="e2d4b2cc-87d5-536f-887a-c8db106f49bb",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SacredCharm.Name",
    display_name="Sacred Charm",
    searchable_by=["Sacred Charm", "Pokémon Tool", "Tool", "SacredCharm"],
    subtypes=["Pokémon Tool", "Tool"],
    collector_number=93,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=SacredCharmPassive(),
)
