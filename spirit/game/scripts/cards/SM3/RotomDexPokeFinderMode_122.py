"""Rotom Dex Poke Finder Mode (SM - Burning Shadows 122/147 -- JP SM3H 047/051, the art here).

Item.

  "Look at the top 4 cards of your deck and put them back in any order.
   You may shuffle your deck instead."

A "Choose 1": rearrange (the private reorder picker) or shuffle. With
0-1 cards on top the rearrangement is moot and only the shuffle is on
offer.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import ItemCardDef

LOOK = 4


async def rotom_dex_poke_finder_mode(ctx):
    top = ctx.deck_top(LOOK)
    if not top:
        return
    which = await ctx.choose(
        "Put the top cards back in any order, or shuffle your deck?",
        ["Put back in any order", "Shuffle your deck"],
        descriptions=[f"Look at the top {len(top)} cards of your deck and put them back in any order.",
                      "Shuffle your deck instead."])
    if which == 0:
        if len(top) <= 1:
            await ctx.session.prompt_view_cards(
                ctx.player_id, ctx.source.entity_id, top, prompt="Top card of your deck")
        else:
            await ctx.reorder_deck_top(LOOK, prompt="Put the cards back in any order")
    else:
        await ctx.shuffle_deck()


card = ItemCardDef(
    guid="7a9088d7-bb7b-5c9b-a546-3983180b1a05",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotomDexPokeFinderMode.Name",
    display_name="Rotom Dex Poké Finder Mode",
    searchable_by=["Rotom Dex Poké Finder Mode", "Rotom Dex", "Item", "RotomDexPokeFinderMode"],
    subtypes=["Item"],
    collector_number=122,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    condition=requires_deck(1),
    effect=rotom_dex_poke_finder_mode,
)
