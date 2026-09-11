"""Erika's Invitation (SV - 151 160/165 -- JP SV2a 161/165, the art here).

Supporter.

  "Look at your opponent's hand. Choose a Basic Pokemon you find there and
   put it onto their Bench. Then, switch it with their Active Pokemon."

Reveal browser over their hand (only the user sees it), a mandatory pick
among the Basics, onto their Bench without on-play triggers (it is "put
onto", not played), then the gust. A full Bench on their side means
nothing can be put down and nothing is switched.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


def _condition(board, player_id, pokemon=None) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    hand = board.find_player_area(opponent, "hand")
    return bool(hand) and bool(hand.children)


async def erikas_invitation(ctx):
    hand = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    basics = [c for c in hand if is_basic_pokemon(c)]
    if not basics:
        return
    bench = ctx.board.find_player_area(ctx.opponent_id, "bench")
    if len(bench.children) >= effective_bench_capacity(ctx.board, ctx.opponent_id):
        return
    picks = await ctx.choose_cards(
        basics, 1, minimum=1,
        prompt="Choose a Basic Pokémon to put onto your opponent's Bench")
    if not picks:
        return
    if not await ctx.bench_pokemon(picks[0]):
        return
    await ctx.flush_choreography()
    await ctx.switch_active(ctx.opponent_id, picks[0], object_is_active=True)


card = SupporterCardDef(
    guid="73ef37e8-b402-520f-b058-f5219d6776af",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasInvitation.Name",
    display_name="Erika's Invitation",
    searchable_by=["Erika's Invitation", "Supporter", "ErikasInvitation"],
    subtypes=["Supporter"],
    collector_number=160,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_condition,
    effect=erikas_invitation,
)
