"""Viridian Forest (SM - Team Up 156/181 -- JP SM9 091/095).

Stadium.

  "Once during each player's turn, that player may discard a card from
   their hand. If they do, that player searches their deck for a basic
   Energy card, reveals it, and puts it into their hand. Then, that player
   shuffles their deck."

Giant Hearth for a basic Energy.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.data_utils import Ability, Activations, StadiumCardDef
from spirit.game.session.effects import is_basic_energy


async def viridian_forest(ctx):
    discarded = await ctx.discard_from_hand(1, prompt="Choose a card to discard for Viridian Forest")
    if not discarded:
        return
    picks = await ctx.search_deck(is_basic_energy, count=1, minimum=0,
                                  prompt="Choose a basic Energy card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = StadiumCardDef(
    guid="2b11ef9f-8d67-51b5-9d4b-803c7f81ce73",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ViridianForest.Name",
    display_name="Viridian Forest",
    searchable_by=["Viridian Forest", "Stadium", "ViridianForest"],
    subtypes=["Stadium"],
    collector_number=156,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Viridian Forest",
        game_text="Once during each player's turn, that player may discard a card from their hand. If they do, that player searches their deck for a basic Energy card, reveals it, and puts it into their hand. Then, that player shuffles their deck.",
        activation=Activations.ONCE_PER_TURN,
        condition=requires_hand(None, 1),
        effect=viridian_forest),
)
