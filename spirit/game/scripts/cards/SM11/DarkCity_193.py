"""Dark City (SM - Unified Minds 193/236 -- JP SMM 030/031, the art here).

Stadium.

  "Basic [D] Pokemon in play (both yours and your opponent's) have no
   Retreat Cost."

Read live off the Pokemon's current types and stage, so a Basic that
stops being Darkness pays again.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import StadiumCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.session.passives import Passive


class DarkCityPassive(Passive):
    """Basic Darkness Pokemon on either side retreat for free."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
            return cost
        if not is_pokemon_of_type(pokemon, PokemonTypes.DARKNESS):
            return cost
        return 0


card = StadiumCardDef(
    guid="f1e591c7-f426-5271-80de-08df573aeca3",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkCity.Name",
    display_name="Dark City",
    searchable_by=["Dark City", "Stadium", "DarkCity"],
    subtypes=["Stadium"],
    collector_number=193,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    passive=DarkCityPassive(),
)
