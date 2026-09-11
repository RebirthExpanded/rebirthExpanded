"""Custom Catcher (SM - Lost Thunder 171/214 -- JP SM7a 055/060).

Item.

  "You may play 2 Custom Catcher cards at once.
   - If you played 1 card, draw cards until you have 3 cards in your hand.
   - If you played 2 cards, switch 1 of your opponent's Benched Pokemon
     with their Active Pokemon.
   (This effect works one time for 2 cards.)"

The client plays one card at a time, so "2 at once" is asked for when the
first one resolves: with a second Custom Catcher in hand and a Bench
opposite to pull from, the player chooses between the one-card draw and
the two-card gust, and choosing the gust plays the second card out of the
hand as part of the same effect -- it is discarded and stamped into the
turn's Trainer ledger like any other Item played. With no second copy, or
with no Bench to pull from, the card is simply the draw.

"Draw cards until you have 3" counts the hand AFTER this card left it,
which is why a hand of 3 draws nothing.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef, def_for

NAME = "Custom Catcher"


def _is_custom_catcher(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == NAME


async def custom_catcher(ctx):
    second = next((c for c in ctx.hand() if _is_custom_catcher(c)), None)
    bench = list(ctx.opponent_bench())
    if second is not None and bench:
        choice = await ctx.choose(
            "Custom Catcher: play 1 or 2?",
            ["Play 1: draw until you have 3 cards",
             "Play 2: switch in 1 of your opponent's Benched Pokémon"])
        if choice == 1:
            await ctx.discard_cards([second])
            ctx.session._record_trainer_played(second)
            target = await ctx.choose_pokemon(
                bench, "Choose the opponent's new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
            return
    await ctx.draw_until(3)


card = ItemCardDef(
    guid="603d499e-bf74-50f6-aa17-463bd261e1b3",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CustomCatcher.Name",
    display_name=NAME,
    searchable_by=[NAME, "Item", "CustomCatcher"],
    subtypes=["Item"],
    collector_number=171,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=custom_catcher,
)
