"""Protection Cube (XY - Flashfire 95/106 -- JP XY2 076/080).

Pokemon Tool.

  "Prevent all damage done to the Pokemon this card is attached to by
   attacks it uses."

Recoil (Roaring Moon ex's Frenzied Gouging, Volt Tackle) does nothing to
the holder; damage from the opponent's attacks is untouched.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class ProtectionCubePassive(Passive):
    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        return bool(calc.is_attack and holder is not None
                    and calc.target is holder and calc.attacker is holder)


card = PokemonToolCardDef(
    guid="ad6258ee-4efb-5611-9656-44948486ce21",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProtectionCube.Name",
    display_name="Protection Cube",
    searchable_by=["Protection Cube", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=95,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    passive=ProtectionCubePassive(),
)
