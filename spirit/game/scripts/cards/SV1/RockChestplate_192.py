"""Rock Chestplate (SV1 192 -- JP SV1S 071; English SVI/192). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.card_effects import passives_common as pc

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.passives import carrier_pokemon


def _fighting_holder(target, carrier) -> bool:
    holder = carrier_pokemon(carrier)
    return target is holder and PokemonTypes.FIGHTING.value in (holder.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonToolCardDef(
    guid="911759c6-74f3-5822-8767-9ec11f36160e",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RockChestplate.Name",
    display_name="Rock Chestplate",
    searchable_by=["Rock Chestplate", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=192,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    passive=pc.takes_less_passive(30, protects=_fighting_holder),
)
