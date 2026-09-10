"""Karen (XY Black Star Promo XY177).

Supporter.

  "Each player shuffles all Pokemon in his or her discard pile into his or
   her deck."

No choosing and no counting: every Pokemon card in both discard piles goes
back, each into its own owner's deck. With no Pokemon in either pile there
is nothing to shuffle back, so the card is not playable.

The pool's first XY Black Star Promo, so Promo_XY joins the Expanded set
list (it was already in sets.json).
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


def _karen_playable(board, player_id, card=None):
    """A Pokemon in either discard pile -- otherwise nothing moves."""
    for pid in board.player_ids:
        discard = board.find_player_area(pid, "discard")
        if any(is_pokemon_card(c) for c in (discard.children if discard else [])):
            return True
    return False


async def karen(ctx):
    """Both discard piles give their Pokemon back."""
    for pid in ctx.board.player_ids:
        discard = ctx.board.find_player_area(pid, "discard")
        pokemon = [c for c in (discard.children if discard else [])
                   if is_pokemon_card(c)]
        if pokemon:
            await ctx.shuffle_into_deck(pokemon, pid)


card = SupporterCardDef(
    guid="7196c79f-70cf-51b4-b1ae-7ae7774c5ee3",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Karen.Name",
    display_name="Karen",
    searchable_by=["Karen", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=karen,
    condition=_karen_playable,
)
