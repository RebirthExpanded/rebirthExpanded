"""Giant Hearth (SM - Unified Minds 197/236 -- JP SM10a 050/054).

Stadium.

  "Once during each player's turn, that player may discard a card from their hand. If they do, that player searches their deck for up to 2 Fire Energy cards, reveals them, and puts them into their hand. Then, that player shuffles their deck."

Any card pays; the search that follows is for the printed [R], so a
Special Energy that provides [R] is not found.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import is_fire_energy_card


async def _discard_then_fire_search(ctx):
    """One card pays; up to 2 [R] Energy come out of the deck for it."""
    discarded = await ctx.discard_from_hand(
        1, prompt="Choose a card to discard for Giant Hearth")
    if not discarded:
        return
    picks = await ctx.search_deck(
        is_fire_energy_card, count=2, minimum=0,
        prompt="Choose up to 2 Fire Energy cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()

from spirit.game.data_utils import Ability, Activations, StadiumCardDef

ABILITY = Ability(
    title="Giant Hearth",
    game_text="Once during each player's turn, that player may discard a card from their hand. If they do, that player searches their deck for up to 2 Fire Energy cards, reveals them, and puts them into their hand. Then, that player shuffles their deck.",
    activation=Activations.ONCE_PER_TURN,
    effect=_discard_then_fire_search,
    condition=requires_hand(None, 1),
)

card = StadiumCardDef(
    guid="49b55c35-f8de-5968-b34b-6630e8f54406",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiantHearth.Name",
    display_name="Giant Hearth",
    searchable_by=["Giant Hearth", "Stadium", "GiantHearth"],
    subtypes=["Stadium"],
    collector_number=197,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    ability=ABILITY,
)
