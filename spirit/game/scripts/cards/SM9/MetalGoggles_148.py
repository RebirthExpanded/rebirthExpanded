"""Metal Goggles (SM - Team Up 148/181 -- JP SM8a 049/052, the art here).

Pokemon Tool.

  "The Pokemon this card is attached to takes 30 less damage from your
   opponent's attacks (after applying Weakness and Resistance), and
   damage counters can't be placed on it by the effects of your
   opponent's attacks or Abilities."

Rigid Band's reduction plus Battle Cage's counter shield, both on the
holder. The shield answers only to an OPPOSING attack's or Ability's
counters (ctx._counters_blocked): the holder's own side, Trainer cards
and plain attack damage still land.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import TakesLessPassive
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.passives import carrier_pokemon

REDUCTION = 30


class MetalGogglesPassive(TakesLessPassive):
    """Holder takes 30 less from opposing attacks; no opposing effect counters."""

    def __init__(self):
        super().__init__(REDUCTION, protects="carrier")

    def blocks_damage_counters(self, target, carrier):
        return carrier_pokemon(carrier) is target


card = PokemonToolCardDef(
    guid="3b246961-f6a1-5fa8-89f2-084d1823c71d",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalGoggles.Name",
    display_name="Metal Goggles",
    searchable_by=["Metal Goggles", "Item", "Pokémon Tool", "MetalGoggles"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=148,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    passive=MetalGogglesPassive(),
)
