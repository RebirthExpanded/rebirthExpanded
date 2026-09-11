"""Maintenance (Generations 64/83 -- JP CP6 079/087).

Item.

  "Shuffle 2 cards from your hand into your deck. (If you can't shuffle 2
   cards into your deck, you can't play this card.) Then, draw a card."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.data_utils import ItemCardDef


async def maintenance(ctx):
    picks = await ctx.choose_cards(
        list(ctx.hand()), 2, minimum=2,
        prompt="Choose 2 cards to shuffle into your deck")
    if len(picks) < 2:
        return
    await ctx.shuffle_into_deck(picks, ctx.player_id)
    await ctx.draw_cards(1)


card = ItemCardDef(
    guid="4481f632-c5df-56d4-98c8-08a0b9ac707b",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name",
    display_name="Maintenance",
    searchable_by=["Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=64,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    condition=requires_hand(None, 2),
    effect=maintenance,
)
