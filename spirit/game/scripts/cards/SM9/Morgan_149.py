"""Morgan (SM - Team Up 149/181 -- JP SM8b 137/150, the art here).

Supporter.

  "You can play this card only if you discard Dana, Evelyn, and Nita from
   your hand (1 each)."
  "Look at the top 12 cards of your deck and attach any number of Energy
   cards you find there to your Pokemon in any way you like. Shuffle the
   other cards back into your deck."

The three sisters are the cost, so they go before the look: the card is
not offered without all three in hand, and the Energy found is
distributed freely (one target chosen per card) rather than piled onto
one Pokemon.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_top_attach_energy
from spirit.game.data_utils import SupporterCardDef, def_for

LOOK = 12
SISTERS = ("Dana", "Evelyn", "Nita")


def _named(card, name: str) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == name


def _sisters_in_hand(board, player_id, card=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    cards = list(hand.children) if hand else []
    return all(any(_named(c, name) for c in cards) for name in SISTERS)


_look = look_top_attach_energy(LOOK, rest="shuffle", distribute=True)


async def morgan(ctx):
    hand = ctx.hand()
    cost = []
    for name in SISTERS:
        match = next((c for c in hand if _named(c, name) and c not in cost), None)
        if match is None:
            return
        cost.append(match)
    await ctx.discard_cards(cost)
    await _look(ctx)


card = SupporterCardDef(
    guid="f154ab74-14ce-5b44-8183-39491a2d1868",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Morgan.Name",
    display_name="Morgan",
    searchable_by=["Morgan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    condition=_sisters_in_hand,
    effect=morgan,
)
