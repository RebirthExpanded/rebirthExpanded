"""Hall of Fame Book (殿堂の書 -- JP SM-P, Pokemon Card Gym "Hall of Fame
Battle" prize; no English print, pool slot Promo_SM 901).

Item.

  "Draw 3 cards. Your turn ends after you play this card."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import ItemCardDef


async def hall_of_fame_book(ctx):
    await ctx.draw_cards(3)
    ctx.ends_turn = True


card = ItemCardDef(
    guid="0946feb2-890e-54c6-a85e-379a3828d6a7",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HallofFameBook.Name",
    display_name="Hall of Fame Book",
    searchable_by=["Hall of Fame Book", "Item", "HallofFameBook"],
    subtypes=["Item"],
    collector_number=901,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    condition=requires_deck(1),
    effect=hall_of_fame_book,
)
