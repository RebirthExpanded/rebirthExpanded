"""Max Revive (XY 120/146 -- JP XY1-Bx 054/060).

Item.

  "Put a Pokemon from your discard pile on top of your deck."

Any Pokemon card, revealed on the way (the Japanese print says so, and
the discard pile is public anyway). Not offered with none there.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import (recover_from_discard,
                                                      requires_discard)
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_pokemon_card

card = ItemCardDef(
    guid="80ee5349-4dc1-5f7f-a556-deed7b3cb5e0",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name",
    display_name="Max Revive",
    searchable_by=["Max Revive", "Item", "MaxRevive"],
    subtypes=["Item"],
    collector_number=120,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(
        is_pokemon_card, count=1, minimum=1, to="deck_top",
        prompt="Choose a Pokémon to put on top of your deck."),
    condition=requires_discard(is_pokemon_card, 1),
)
