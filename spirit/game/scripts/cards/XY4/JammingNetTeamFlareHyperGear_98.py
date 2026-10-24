"""Jamming Net Team Flare Hyper Gear (XY - Phantom Forces 98/119).

Pokemon Tool (Team Flare Hyper Gear).

  "Attach this Pokemon Tool to 1 of your opponent's Pokemon-EX that
   doesn't already have a Pokemon Tool attached to it."
  "The attacks of the Pokemon this card is attached to do 20 less damage to
   all Defending Pokemon (before applying Weakness and Resistance)."
  "When this card is removed from a Pokemon for any reason, put this card
   in its owner's discard pile."

Head Ringer's twin; "Defending Pokemon" is the opponent's Active.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef, subtypes_for
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_pokemon_ex(pokemon) -> bool:
    return "EX" in (subtypes_for(pokemon.archetype_id) or [])


class JammingNetPassive(Passive):
    def modify_damage_dealt(self, calc, carrier):
        if calc.is_attack and calc.is_opposing and calc.to_active                 and carrier_pokemon(carrier) is calc.attacker:
            calc.amount = max(0, calc.amount - 20)


card = PokemonToolCardDef(
    guid="7aa161b2-aaae-5755-a67a-22aa1a51104b",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JammingNetTeamFlareHyperGear.Name",
    display_name="Jamming Net Team Flare Hyper Gear",
    searchable_by=["Jamming Net Team Flare Hyper Gear", "Jamming Net", "Pokémon Tool", "Team Flare Hyper Gear"],
    subtypes=["Pokémon Tool", "Team Flare Hyper Gear"],
    collector_number=98,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    attach_to_opponent=True,
    discard_when_removed=True,
    attach_to=_is_pokemon_ex,
    passive=JammingNetPassive(),
)
