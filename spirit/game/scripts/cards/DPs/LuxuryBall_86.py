"""Luxury Ball (DP - Stormfront 86/100 -- JP DPs 081/092, the art here).

Item.

  "Search your deck for a Pokemon, reveal it, and put it into your hand.
   Then, shuffle your deck. If any Luxury Ball is in your discard pile,
   you can't play this card."

The printed "(excluding Pokemon LV.X)" has nothing to exclude in this
pool. The self-lock reads the discard pile by name, so a second copy is
dead once the first one is used. The low-resolution art is all
pokemon-card.com carries for this print.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.session.effects import is_pokemon_card

NAME = "Luxury Ball"


def _no_luxury_ball_in_discard(board, player_id) -> bool:
    pile = board.find_player_area(player_id, "discard")
    return not any(
        getattr(def_for(c.archetype_id), "display_name", None) == NAME
        for c in (pile.children if pile else []))


card = ItemCardDef(
    guid="2e3cd5af-89b1-55e2-b09d-1a3c693bf331",
    key="DPs",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuxuryBall.Name",
    display_name=NAME,
    searchable_by=["Luxury Ball", "Item", "LuxuryBall"],
    subtypes=["Item"],
    collector_number=86,
    set_code="DPs",
    rarity=Rarities.Uncommon,
    condition=_no_luxury_ball_in_discard,
    effect=search_to_hand(is_pokemon_card, count=1, minimum=0, reveal=True,
                          prompt="Choose a Pokémon to put into your hand."),
)
