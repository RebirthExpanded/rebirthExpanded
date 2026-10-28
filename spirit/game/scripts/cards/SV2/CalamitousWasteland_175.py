"""Calamitous Wasteland (SV2 175 -- JP SV2D 070; English PAL/175). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import is_basic_pokemon_in_play


class CalamitousWastelandPassive(Passive):
    """Basic non-Fighting Pokemon in play: Retreat Cost [C] more."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if is_basic_pokemon_in_play(pokemon) and PokemonTypes.FIGHTING.value not in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or []):
            return cost + 1
        return cost


card = StadiumCardDef(
    guid="0b37a5d0-238f-539d-842a-8a525ead847c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CalamitousWasteland.Name",
    display_name="Calamitous Wasteland",
    searchable_by=["Calamitous Wasteland", "Stadium"],
    subtypes=["Stadium"],
    collector_number=175,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    passive=CalamitousWastelandPassive(),
)
