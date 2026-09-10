"""Devolution Spray Z (SM - Unbroken Bonds 166/214 -- JP SM9b 044/054).

Item.

  "Devolve 1 of your evolved Pokemon by shuffling any number of Evolution
   cards on it into your deck. (That Pokemon can't evolve this turn.)"

Devolution Spray with two differences: as many steps as you like, and the
cards go back into the DECK rather than your hand -- so a Stage 2 can come
all the way down to its Basic in one go, and what comes off is shuffled
away rather than re-playable.

devolve_depth is how far down the stack goes, so the chooser offers 1 to
that many steps and stops there. As with every devolution the damage stays
with the Pokemon that remains.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import devolvable, devolve_depth
from spirit.game.data_utils import ItemCardDef


def _has_devolvable_pokemon(board, player_id, card=None):
    return any(devolvable(p) for p in board.pokemon_in_play(player_id))


async def devolution_spray_z(ctx):
    """As many steps down as the player likes; the cards go into the deck."""
    candidates = [p for p in ctx.my_pokemon_in_play() if devolvable(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your evolved Pokémon to devolve.")
    if target is None:
        return
    depth = devolve_depth(target)
    if depth <= 0:
        return
    steps = depth
    if depth > 1:
        options = [f"{n} card{'s' if n > 1 else ''}" for n in range(1, depth + 1)]
        choice = await ctx.choose(
            "How many Evolution cards do you want to shuffle away?", options)
        steps = (choice + 1) if choice is not None else depth
    await ctx.devolve_pokemon(target, steps=steps, destination="deck")
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="5c8d8ea9-358f-535b-a954-0817b0c9730d",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSprayZ.Name",
    display_name="Devolution Spray Z",
    searchable_by=["Devolution Spray Z", "Item", "DevolutionSprayZ"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=devolution_spray_z,
    condition=_has_devolvable_pokemon,
)
