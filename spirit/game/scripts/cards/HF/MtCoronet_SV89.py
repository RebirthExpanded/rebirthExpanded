"""Mt. Coronet (SM - Ultra Prism 130/156 -- JP SM5S 064/066, the art here).

Stadium.

  "Once during each player's turn, that player may put 2 [M] Energy cards
   from their discard pile into their hand."

Both players; the pick is shown to the opponent (the JP text says so and
the pile is public anyway). Fewer than 2 there: take what is there. Only
[M] Energy cards (is_energy_of_type: a basic Metal Energy, or a Special
Energy that is a [M] Energy card) -- it took any Energy before.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, Activations, StadiumCardDef
from spirit.game.attributes import PokemonTypes
from spirit.game.session.effects import is_energy_of_type

TAKE = 2


def _metal_energy(card) -> bool:
    return is_energy_of_type(card, PokemonTypes.METAL)


def _energy_in_discard(board, player_id, stadium=None) -> bool:
    pile = board.find_player_area(player_id, "discard")
    return any(_metal_energy(c) for c in (pile.children if pile else []))


async def mt_coronet(ctx):
    pool = [c for c in ctx.recoverable_discard() if _metal_energy(c)]
    if not pool:
        return
    take = min(TAKE, len(pool))
    picks = await ctx.choose_cards(
        pool, take, minimum=take,
        prompt="Choose 2 Metal Energy cards to put into your hand.")
    await ctx.put_in_hand(picks or pool[:take], reveal=True)


ABILITY = Ability(
    title="Mt. Coronet",
    game_text="Once during each player's turn, that player may put 2 [M] Energy cards from their discard pile into their hand.",
    activation=Activations.ONCE_PER_TURN,
    effect=mt_coronet,
    condition=_energy_in_discard,
)

card = StadiumCardDef(
    guid="7149eb36-4b7f-5cae-aef6-7507bda35ab6",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtCoronet.Name",
    display_name="Mt. Coronet",
    searchable_by=["Mt. Coronet", "Stadium", "MtCoronet"],
    subtypes=["Stadium"],
    collector_number=158,
    set_code="HF",
    rarity=Rarities.RareSecret,
    ability=ABILITY,
)
