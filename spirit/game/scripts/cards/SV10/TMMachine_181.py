"""TM Machine (SV - Destined Rivals 181/182 -- JP SV-P 189, the art here).

Item.

  "Search your deck for up to 3 Pokemon Tool cards that have 'Technical
   Machine' in their name, reveal them, and put them into your hand.
   Then, shuffle your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.session.effects import is_pokemon_tool


def _technical_machine_tool(card) -> bool:
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return is_pokemon_tool(card) and "Technical Machine" in name


card = ItemCardDef(
    guid="90f4dc01-3663-5743-80ac-c2241ea47756",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TMMachine.Name",
    display_name="TM Machine",
    searchable_by=["TM Machine", "Item", "TMMachine"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(_technical_machine_tool, count=3, minimum=0, reveal=True,
                          prompt="Choose up to 3 Technical Machine Pokémon Tools."),
)
