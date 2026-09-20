"""Metal Frying Pan (SM - Lost Thunder 144/214 -- JP SM8b 124/150, the art here).

Pokemon Tool.

  "The Pokemon this card is attached to takes 30 less damage from your
   opponent's attacks (after applying Weakness and Resistance) and has no
   Weakness."

Rigid Band's reduction plus Mysterious Nest's no-Weakness, both riding
the holder; one Passive so Tool Jammer switches them off together.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import (NoWeaknessPassive,
                                                      TakesLessPassive)
from spirit.game.data_utils import PokemonToolCardDef

REDUCTION = 30


class MetalFryingPanPassive(TakesLessPassive):
    """Holder takes 30 less from opposing attacks and has no Weakness."""

    def __init__(self):
        super().__init__(REDUCTION, protects="carrier")
        self._no_weakness = NoWeaknessPassive(protects="carrier")

    def modify_weakness(self, calc, carrier):
        self._no_weakness.modify_weakness(calc, carrier)


card = PokemonToolCardDef(
    guid="48946b6b-891a-56f3-83c1-2f2dd57da5ec",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalFryingPan.Name",
    display_name="Metal Frying Pan",
    searchable_by=["Metal Frying Pan", "Item", "Pokémon Tool", "MetalFryingPan"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=144,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    passive=MetalFryingPanPassive(),
)
