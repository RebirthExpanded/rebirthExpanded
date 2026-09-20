"""Missing Clover (SM - Ultra Prism 129/156 -- JP SM5S 058/066, the art here).

Item.

  "You may play 4 Missing Clover at once. If you play 1 Missing Clover,
   look at the top card of your deck. If you play 4 Missing Clover at
   once, take a Prize card."

The client plays one card at a time, so "4 at once" is a choice offered
on the first one when 3 more sit in hand: the other 3 are discarded
together with it and a Prize is taken (the prize-take window opens as
for any other take). Otherwise a private look at the top card.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef, def_for

NAME = "Missing Clover"
SET_OF = 4


def _other_clovers(ctx):
    return [c for c in ctx.hand()
            if c is not ctx.source
            and getattr(def_for(c.archetype_id), "display_name", None) == NAME]


async def missing_clover(ctx):
    others = _other_clovers(ctx)
    if len(others) >= SET_OF - 1:
        which = await ctx.choose(
            "Play 1 Missing Clover, or 4 at once?",
            ["Play 1", "Play 4 at once"],
            descriptions=["Look at the top card of your deck.",
                          "Discard 3 more Missing Clover from your hand and take a Prize card."])
        if which == 1:
            await ctx.discard_cards(others[:SET_OF - 1])
            await ctx.take_prizes(1)
            return
    top = ctx.deck_top(1)
    if top:
        await ctx.session.prompt_view_cards(
            ctx.player_id, ctx.source.entity_id, top, prompt="Top card of your deck")


card = ItemCardDef(
    guid="ee3f050d-ba72-5b0b-ba2b-317cd377768e",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MissingClover.Name",
    display_name=NAME,
    searchable_by=["Missing Clover", "Item", "MissingClover"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=missing_clover,
)
