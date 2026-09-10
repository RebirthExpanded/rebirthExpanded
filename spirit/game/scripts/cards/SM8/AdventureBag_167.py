"""Adventure Bag (SM - Lost Thunder 167/214 -- JP SM7b 043/050).

Item.

  "Search your deck for up to 2 Pokemon Tool cards, reveal them, and put
   them into your hand. Then, shuffle your deck."

search_to_hand with the Tool predicate, no more. What it reaches is worth
saying: under this pool's rule that every Pokemon Tool is a Pokemon Tool
and never an Item, is_pokemon_tool reads the printed category, so Float
Stone and Hero's Cape come out of the deck alongside Technical Machine:
Evolution and Crisis Punch.

"Up to 2" is minimum=0, so it is playable with no Tool in the deck (the
deck still opens, the player still looks) -- the empty-deck gate covers
the only case where nothing can happen at all.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_pokemon_tool

card = ItemCardDef(
    guid="371cb980-8179-5253-b733-0fdbf92974c5",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdventureBag.Name",
    display_name="Adventure Bag",
    searchable_by=["Adventure Bag", "Item", "AdventureBag"],
    subtypes=["Item"],
    collector_number=167,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        is_pokemon_tool, count=2, minimum=0,
        prompt="Choose up to 2 Pokémon Tool cards to put into your hand.",
    ),
)
