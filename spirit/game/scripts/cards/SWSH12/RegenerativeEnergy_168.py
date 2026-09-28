"""Regenerative Energy (SWSH - Silver Tempest 168/195).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [C] Energy.
   Whenever you play a Pokemon from your hand to evolve the Pokemon V this
   card is attached to, heal 100 damage from that Pokemon."

Wyndon Stadium's heal_on_evolve hook, which the engine asks only for an
evolution played from hand: the card must ride the evolved stack and the
Pokemon it evolved from must be a Pokemon V.
"""

from spirit.game.data_utils import EnergyCardDef, is_pokemon_v
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class RegenerativeEnergyPassive(Passive):
    def heal_on_evolve(self, evolved, pre_evolution, player_id, carrier):
        if carrier_pokemon(carrier) is not evolved:
            return 0
        if evolved.owning_player_id != player_id:
            return 0
        if not is_pokemon_v(pre_evolution.archetype_id):
            return 0
        return 100


card = EnergyCardDef(
    guid="d5be181e-eb89-50ba-8e6e-cff7aa95420b",
    key="SWSH12",
    name="Regenerative Energy",
    display_name="Regenerative Energy",
    searchable_by=["Regenerative Energy", "Special"],
    subtypes=["Special"],
    collector_number=168,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=RegenerativeEnergyPassive(),
)
