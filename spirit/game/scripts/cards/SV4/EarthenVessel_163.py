"""Earthen Vessel (SV - Paradox Rift 163/182 -- JP SV4K 060/066).

Item.  "You can use this card only if you discard another card from your
hand. Search your deck for up to 2 Basic Energy cards, reveal them, and
put them into your hand. Then, shuffle your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_basic_energy


async def earthen_vessel(ctx):
    paid = await ctx.discard_from_hand(1, prompt="Discard a card for Earthen Vessel")
    if not paid:
        return
    picks = await ctx.search_deck(is_basic_energy, count=2, minimum=0,
                                  prompt="Choose up to 2 Basic Energy cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="3becdac8-8b71-564c-a4d5-824cc703ca9f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EarthenVessel.Name",
    display_name="Earthen Vessel",
    searchable_by=["Earthen Vessel", "Item", "EarthenVessel"],
    subtypes=["Item"],
    collector_number=163,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    condition=requires_hand(None, 1),
    effect=earthen_vessel,
)
