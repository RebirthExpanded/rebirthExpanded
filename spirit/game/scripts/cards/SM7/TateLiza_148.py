"""Tate & Liza (SM - Celestial Storm 148/168 -- JP SM7 083/096).

Supporter.

  "Choose 1:
   - Shuffle your hand into your deck. Then, draw 5 cards.
   - Switch your Active Pokemon with 1 of your Benched Pokemon."

The choice is made up front. With no Bench the switch half is not offered
and the card is the draw; the draw half is always available.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw
from spirit.game.card_effects.trainers import switch
from spirit.game.data_utils import SupporterCardDef

_draw_five = shuffle_hand_into_deck_draw(5)


async def tate_and_liza(ctx):
    """Draw 5 off a fresh hand, or switch."""
    if not ctx.my_bench():
        await _draw_five(ctx)
        return
    choice = await ctx.choose(
        "Tate & Liza: choose 1.",
        ["Shuffle your hand into your deck and draw 5",
         "Switch your Active Pokémon"])
    if choice == 1:
        await switch(ctx)
    else:
        await _draw_five(ctx)


card = SupporterCardDef(
    guid="f3dcd0c4-a148-5f22-b88c-75d2a9d72dcf",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TateLiza.Name",
    display_name="Tate & Liza",
    searchable_by=["Tate & Liza", "Supporter", "TateLiza"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=tate_and_liza,
)
