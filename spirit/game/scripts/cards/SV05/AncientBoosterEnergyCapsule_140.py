"""Ancient Booster Energy Capsule (SV - Temporal Forces 140/162 -- JP SV5K
065/071).

Pokemon Tool.  "The Ancient Pokemon this card is attached to gets +60 HP,
recovers from all Special Conditions, and can't be affected by any
Special Conditions."

The +60 and the immunity are continuous; the one-time "recovers" on
attach is not wired (Tools have no on-attach hook yet) -- a Special
Condition already on the holder stays until it would normally end.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef, subtypes_for
from spirit.game.session.passives import Passive, carrier_pokemon


def _ancient(pokemon) -> bool:
    return "Ancient" in subtypes_for(pokemon.archetype_id)


class AncientBoosterPassive(Passive):
    def max_hp_bonus(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        return 60 if holder is pokemon and _ancient(holder) else 0

    def blocks_special_conditions(self, target, condition, carrier):
        holder = carrier_pokemon(carrier)
        return holder is target and _ancient(holder)


card = PokemonToolCardDef(
    guid="f32a8152-1da5-5980-8955-eb4309d81f2a",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientBoosterEnergyCapsule.Name",
    display_name="Ancient Booster Energy Capsule",
    searchable_by=["Ancient Booster Energy Capsule", "Pokémon Tool", "AncientBoosterEnergyCapsule"],
    subtypes=["Pokémon Tool"],
    collector_number=140,
    set_code="SV05",
    rarity=Rarities.Uncommon,
    regulation_mark="H",
    passive=AncientBoosterPassive(),
)
