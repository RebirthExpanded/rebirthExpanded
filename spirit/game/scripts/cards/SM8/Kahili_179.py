"""Kahili (SM - Lost Thunder 179/214 -- JP SM7a 055/060).

Supporter.

  "Draw 2 cards. Then, flip a coin. If heads, if you played this Kahili from
   your hand, put this card into your hand instead of the discard pile.
   If you have no cards in your deck, you can't play this card."

"Played from your hand" is this card sitting in the Trainer slot: an effect
that borrows Kahili's text (Smeargle's Stunning Likeness) draws and flips
but has no Kahili to return. A card the effect moved is not discarded
afterwards (Egg Incubator's shape).
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.data_utils import SupporterCardDef


def _deck_not_empty(board, player_id, card=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def kahili(ctx):
    await ctx.draw_cards(2)
    heads = (await ctx.flip_coins(1, "Kahili"))[0]
    source = ctx.source
    parent = getattr(source, "parent", None)
    played = (getattr(ctx, "is_trainer_effect", False) and parent is not None
              and parent.get_attribute(AttrID.NAME) == "activeTrainer")
    if heads and played:
        await ctx.put_in_hand([source], reveal=True)


card = SupporterCardDef(
    guid="8853c96a-9146-539e-8652-9684512b61ae",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kahili.Name",
    display_name="Kahili",
    searchable_by=["Kahili", "Supporter"],
    subtypes=["Supporter"],
    collector_number=179,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    condition=_deck_not_empty,
    effect=kahili,
)
