"""Devolution Spray (BW - Dragons Exalted 113/124 -- JP BW5 048/050).

Item.

  "Devolve 1 of your evolved Pokemon and put the highest stage Evolution
   card on it into your hand. (That Pokemon can't evolve this turn.)"

One step off one of YOUR Pokemon, and the card comes back to hand rather
than to the deck -- which is the point: the evolution is re-playable, and
the damage stays on the Pokemon underneath.

The parenthesis is not this card's own bookkeeping any more: every card
that devolves prints it, so perform_devolution now stamps the remaining
stage as devolved-this-turn and the evolve gate reads that. It is kept
apart from "came into play this turn", which cards asking whether a
Pokemon EVOLVED this turn read -- a devolved Pokemon did not.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import devolvable
from spirit.game.data_utils import ItemCardDef


def _has_devolvable_pokemon(board, player_id, card=None):
    return any(devolvable(p) for p in board.pokemon_in_play(player_id))


async def devolution_spray(ctx):
    """One step down, the top card to hand."""
    candidates = [p for p in ctx.my_pokemon_in_play() if devolvable(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your evolved Pokémon to devolve.")
    if target is None:
        return
    await ctx.devolve_pokemon(target, steps=1, destination="hand")


card = ItemCardDef(
    guid="07effd5c-2b19-5c17-b54f-6b39113370bd",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSpray.Name",
    display_name="Devolution Spray",
    searchable_by=["Devolution Spray", "Item", "DevolutionSpray"],
    subtypes=["Item"],
    collector_number=113,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    effect=devolution_spray,
    condition=_has_devolvable_pokemon,
)
