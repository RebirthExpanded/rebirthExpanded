"""Roller Skater (SM - Cosmic Eclipse 203/236 -- JP SM11a 058/064).

Supporter.

  "Discard a card from your hand. If you do, draw 2 cards. If you discarded
   an Energy card in this way, draw 2 more cards."

Needs another card in hand to discard.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_size_at_least
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import is_energy_card


async def roller_skater(ctx):
    picks = await ctx.discard_from_hand(1, prompt="Choose a card to discard")
    if not picks:
        return
    await ctx.draw_cards(4 if is_energy_card(picks[0]) else 2)


card = SupporterCardDef(
    guid="c1c6de0a-140b-5ce0-9e3c-3aa212fc2e42",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RollerSkater.Name",
    display_name="Roller Skater",
    searchable_by=["Roller Skater", "Supporter", "RollerSkater"],
    subtypes=["Supporter"],
    collector_number=203,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    condition=hand_size_at_least(2),
    effect=roller_skater,
)
