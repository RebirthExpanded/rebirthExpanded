"""Hole-Digging Shovel (ME - POR 74 -- JP M-P promo, the art here).

Item.

  "Discard the top 2 cards of your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import ItemCardDef


async def hole_digging_shovel(ctx):
    top = ctx.deck_top(2)
    if top:
        await ctx.discard_cards(top)


card = ItemCardDef(
    guid="6565fd0d-07df-5fe6-8976-f99ea525d567",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HoleDiggingShovel.Name",
    display_name="Hole-Digging Shovel",
    searchable_by=["Hole-Digging Shovel", "Item", "HoleDiggingShovel"],
    subtypes=["Item"],
    collector_number=74,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    condition=requires_deck(1),
    effect=hole_digging_shovel,
)
