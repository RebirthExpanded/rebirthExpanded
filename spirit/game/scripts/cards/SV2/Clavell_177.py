"""Clavell (SV2 177 -- JP SV1a 067; English PAL/177, PAL/249). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects import support_common as su

from spirit.game.attributes import AttrID
from spirit.game.session.effects import is_basic_pokemon


def _small_basic(card) -> bool:
    return is_basic_pokemon(card) and (card.get_attribute(AttrID.HP, 0) or 0) <= 120


card = SupporterCardDef(
    guid="9cb1ef98-07dc-561b-8301-340d37458bfe",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clavell.Name",
    display_name="Clavell",
    searchable_by=["Clavell", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    effect=su.search_to_hand(_small_basic, count=3, reveal=True, prompt="Choose up to 3 Basic Pokémon with 120 HP or less."),
)
