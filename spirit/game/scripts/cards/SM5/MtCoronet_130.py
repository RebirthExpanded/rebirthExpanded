"""Mt. Coronet (SM - Ultra Prism 130/156 -- JP SM5S 064/066, the art here).

Stadium.

  "Once during each player's turn, that player may put 2 Energy cards
   from their discard pile into their hand."

Both players; the pick is shown to the opponent (the JP text says so and
the pile is public anyway). Fewer than 2 there: take what is there.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, Activations, StadiumCardDef
from spirit.game.session.effects import is_energy_card

TAKE = 2


def _energy_in_discard(board, player_id, stadium=None) -> bool:
    pile = board.find_player_area(player_id, "discard")
    return any(is_energy_card(c) for c in (pile.children if pile else []))


async def mt_coronet(ctx):
    pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
    if not pool:
        return
    take = min(TAKE, len(pool))
    picks = await ctx.choose_cards(
        pool, take, minimum=take,
        prompt="Choose 2 Energy cards to put into your hand.")
    await ctx.put_in_hand(picks or pool[:take], reveal=True)


ABILITY = Ability(
    title="Mt. Coronet",
    game_text="Once during each player's turn, that player may put 2 Energy cards from their discard pile into their hand.",
    activation=Activations.ONCE_PER_TURN,
    effect=mt_coronet,
    condition=_energy_in_discard,
)

card = StadiumCardDef(
    guid="9f44d9ce-9fb7-513c-a8b3-a2c6c626e369",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtCoronet.Name",
    display_name="Mt. Coronet",
    searchable_by=["Mt. Coronet", "Stadium", "MtCoronet"],
    subtypes=["Stadium"],
    collector_number=130,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    ability=ABILITY,
)
