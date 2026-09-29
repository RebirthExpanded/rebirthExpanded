"""Perilous Jungle (SV - Temporal Forces 156/162 -- JP SV5K 070/071).

Stadium.

  "During Pokemon Checkup, put 2 more damage counters on each Poisoned
   non-[D] Pokemon (both yours and your opponent's)."
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import StadiumCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.session.passives import Passive


class PerilousJunglePassive(Passive):
    def modify_poison_counters(self, counters, pokemon, carrier):
        if is_pokemon_of_type(pokemon, PokemonTypes.DARKNESS):
            return counters
        return counters + 2


card = StadiumCardDef(
    guid="7119acda-08a5-55b1-b49b-bb660fc6bb43",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PerilousJungle.Name",
    display_name="Perilous Jungle",
    searchable_by=["Perilous Jungle", "Stadium", "PerilousJungle"],
    subtypes=["Stadium"],
    collector_number=156,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=PerilousJunglePassive(),
)
