"""Wide Lens (XY - Roaring Skies 95/108 -- JP XY6-B 072/078).

Pokemon Tool.

  "Damage from the attacks of the Pokemon this card is attached to is
   affected by Weakness and Resistance for your opponent's Benched
   Pokemon."

Turns Weakness/Resistance back on for the holder's Bench hits that
skipped them only because of the rules parenthetical "(Don't apply
Weakness and Resistance for Benched Pokemon.)" -- Raikou's Amazing Shot,
any spread. An attack whose own effect says its damage "isn't affected by
Weakness or Resistance" (Alolan Raichu's Electro Rain) is unchanged: the
lens does not override an attack's text.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class WideLensPassive(Passive):
    def applies_bench_modifiers(self, calc, carrier):
        return calc.attacker is not None and calc.attacker is carrier_pokemon(carrier)


card = PokemonToolCardDef(
    guid="26eee8fb-98b6-50f4-b430-478eee2066f0",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WideLens.Name",
    display_name="Wide Lens",
    searchable_by=["Wide Lens", "Pokémon Tool", "WideLens"],
    subtypes=["Pokémon Tool"],
    collector_number=95,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    passive=WideLensPassive(),
)
