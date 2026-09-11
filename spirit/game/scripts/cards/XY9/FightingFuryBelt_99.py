"""Fighting Fury Belt (XY - BREAKpoint 99/122 -- JP XY9-B 071/080).

Pokemon Tool.

  "The Basic Pokemon this card is attached to gets +40 HP and its attacks do
   10 more damage to your opponent's Active Pokemon (before applying Weakness
   and Resistance)."

Both halves answer only while the holder is a Basic as it sits on the
board (a fossil counts; an evolved holder loses both, and the engine keeps
the damage taken constant when the +40 goes away).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.effects import is_basic_pokemon_in_play
from spirit.game.session.passives import Passive, carrier_pokemon


class FightingFuryBeltPassive(Passive):
    def max_hp_bonus(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not pokemon or not is_basic_pokemon_in_play(holder):
            return 0
        return 40

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        holder = carrier_pokemon(carrier)
        if holder is not calc.attacker or not is_basic_pokemon_in_play(holder):
            return
        calc.amount += 10


card = PokemonToolCardDef(
    guid="459499e0-07f0-5aed-9c9c-b5ff4e9ec82d",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingFuryBelt.Name",
    display_name="Fighting Fury Belt",
    searchable_by=["Fighting Fury Belt", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=99,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    passive=FightingFuryBeltPassive(),
)
