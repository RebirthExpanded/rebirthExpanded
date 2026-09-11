"""Energy Spinner (SM - Unbroken Bonds 170/214 -- JP SM-P promo pack 6).

Item.

  "Search your deck for a basic Energy card, reveal it, and put it into
   your hand. If you go second and it's your first turn, search for up to
   3 basic Energy cards instead of 1. Then, shuffle your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_basic_energy


async def energy_spinner(ctx):
    ts = ctx.session.turn_state
    count = 3 if ts.turn_number == 2 else 1
    picks = await ctx.search_deck(is_basic_energy, count=count, minimum=0,
                                  prompt=f"Choose up to {count} basic Energy card(s) to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="16839404-5785-57aa-a5d8-81cb575976d8",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySpinner.Name",
    display_name="Energy Spinner",
    searchable_by=["Energy Spinner", "Item", "EnergySpinner"],
    subtypes=["Item"],
    collector_number=170,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=requires_deck(1),
    effect=energy_spinner,
)
