"""Treasure Tracker (SV085 131 -- JP SV8a 146; English PRE/131). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_pokemon_tool


card = ItemCardDef(
    guid="d802ab4a-98d6-5bd7-8c23-7bf6ae572def",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TreasureTracker.Name",
    display_name="Treasure Tracker",
    searchable_by=["Treasure Tracker", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=131,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=su.search_to_hand(is_pokemon_tool, count=5, reveal=True, prompt="Choose up to 5 Pokémon Tool cards."),
)
