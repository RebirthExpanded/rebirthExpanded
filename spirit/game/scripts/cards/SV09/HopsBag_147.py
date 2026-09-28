"""Hop's Bag (SV - Journey Together 147/190 -- JP SV9 091/100).

Item.

  "Search your deck for up to 2 Basic Hop's Pokemon and put them onto your
   Bench. Then, shuffle your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.session.effects import is_basic_pokemon


def _basic_hops(card) -> bool:
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return is_basic_pokemon(card) and name.startswith("Hop's ")


card = ItemCardDef(
    guid="7d0d7ec0-fc40-5d08-a704-3e96e39fa2c9",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HopsBag.Name",
    display_name="Hop's Bag",
    searchable_by=["Hop's Bag", "Item", "HopsBag"],
    subtypes=["Item"],
    collector_number=147,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(predicate=_basic_hops, count=2,
                           prompt="Choose up to 2 Basic Hop's Pokémon to put onto your Bench."),
)
