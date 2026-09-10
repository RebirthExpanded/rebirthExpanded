"""Cynthia & Caitlin (SM - Cosmic Eclipse 189/236).

Supporter, TAG TEAM.

  "Put a Supporter card from your discard pile into your hand. You can't
   choose Cynthia & Caitlin or a card you discarded with the effect of
   this card."
  "When you play this card, you may discard another card from your hand.
   If you do, draw 3 cards."

The optional discard resolves first -- it is the "when you play this
card" rider, and the exclusion clause only makes sense that way round:
the card you just paid cannot be the Supporter you pick back up. So the
order is discard -> draw 3 -> recover, and the recovery's candidate list
is taken AFTER the discard so the paid card is naturally in it, then
filtered out by identity.

Two exclusions, and they are different kinds:

  * the paid card, by IDENTITY -- only that copy, and only when it was a
    Supporter at all (paying a Pokemon excludes nothing);
  * Cynthia & Caitlin, by NAME -- every copy in the discard, not just this
    one. The copy being played is still on the trainer slot and reaches
    the discard afterwards, so it is not a candidate either way, but an
    earlier copy would be without this.

The recovery is mandatory when a legal Supporter exists ("Put a Supporter
card...", not "you may"), so minimum=1. Unlike VS Seeker this card has no
condition: the discard-and-draw half stands on its own, so it is still
worth playing with an empty discard pile.
"""

from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_supporter_card

CYNTHIA_AND_CAITLIN = "Cynthia & Caitlin"


async def cynthia_and_caitlin(ctx):
    """Optionally pay a card to draw 3, then take a Supporter back."""
    paid = []
    if ctx.hand() and await ctx.ask_yes_no(
            "Discard a card to draw 3 cards?"):
        paid = await ctx.discard_from_hand(
            1, minimum=1, prompt="Choose a card to discard")
        if paid:
            await ctx.draw_cards(3)

    paid_ids = {c.entity_id for c in paid}

    def takeable(card) -> bool:
        if not is_supporter_card(card) or card.entity_id in paid_ids:
            return False
        definition = def_for(card.archetype_id)
        return getattr(definition, "display_name", None) != CYNTHIA_AND_CAITLIN

    candidates = [c for c in ctx.discard_pile() if takeable(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Supporter card to put into your hand.",
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = SupporterCardDef(
    guid="e9c83471-65c5-5038-b053-46426391fc43",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiaCaitlin.Name",
    display_name=CYNTHIA_AND_CAITLIN,
    searchable_by=["Cynthia & Caitlin", "Supporter", "TAG TEAM",
                   "CynthiaCaitlin"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=189,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=cynthia_and_caitlin,
)
