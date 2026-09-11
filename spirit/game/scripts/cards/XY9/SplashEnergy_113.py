"""Splash Energy (XY - BREAKpoint 113/122 -- JP XY9-B 080/080).

Special Energy.

  "This card can only be attached to [W] Pokemon. This card provides [W]
   Energy only while this card is attached to a [W] Pokemon. If the [W]
   Pokemon this card is attached to is Knocked Out by damage from an
   opponent's attack, put that Pokemon into your hand. (Discard all cards
   attached to it.) (If this card is attached to anything other than a [W]
   Pokemon, discard this card.)"

The return-to-hand rides knockout_destination, reading the flag the
knockout resolver stamps on a Pokemon Knocked Out by damage from an
opposing attack; everything attached falls to the discard pile.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_water(pokemon) -> bool:
    return is_pokemon_of_type(pokemon, PokemonTypes.WATER)


class SplashEnergyPassive(Passive):
    def knockout_destination(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon or not _is_water(pokemon):
            return None
        return "hand" if getattr(pokemon, "ko_by_opposing_attack_damage", False) else None


card = EnergyCardDef(
    guid="9bb3a64f-49e2-54e8-af6e-383d557d1d08",
    key="XY9",
    name="Splash Energy",
    display_name="Splash Energy",
    searchable_by=["Splash Energy", "Special", "SplashEnergy"],
    subtypes=["Special"],
    collector_number=113,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.WATER,
    is_special=True,
    provides=[[PokemonTypes.WATER]],
    attach_to=_is_water,
    discard_if_invalid=True,
    passive=SplashEnergyPassive(),
)
