"""Heavy Ball (BW - Next Destinies 88/99 -- JP BW3-Bh 049/052).

Item.

  "Search your deck for a Pokemon with a Retreat Cost of 3 or more, reveal
   it, and put it into your hand. Shuffle your deck afterward."

The PRINTED Retreat Cost on the card in the deck, the same reading Feather
Ball takes from the other end of the scale: nothing in play is involved, so
Float Stone and friends do not enter into it.
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_pokemon_card


def _heavy_pokemon(card) -> bool:
    return (is_pokemon_card(card)
            and int(card.get_attribute(AttrID.RETREAT_COST) or 0) >= 3)


card = ItemCardDef(
    guid="952764bc-dcf9-56b5-90da-23abc0d1f776",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeavyBall.Name",
    display_name="Heavy Ball",
    searchable_by=["Heavy Ball", "Item", "HeavyBall"],
    subtypes=["Item"],
    collector_number=88,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _heavy_pokemon, count=1, minimum=0,
        prompt="Choose a Pokémon with a Retreat Cost of 3 or more."),
)
