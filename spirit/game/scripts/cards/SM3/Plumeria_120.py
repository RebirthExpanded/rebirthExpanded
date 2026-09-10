"""Plumeria (SM - Burning Shadows 120/147).

Supporter.

  "Discard 2 cards from your hand. If you do, discard an Energy from 1 of
   your opponent's Pokemon."

The discard is the cost and the "If you do" hangs off it, so both halves
have to be possible for the card to be playable: 2 other cards in hand,
and an Energy attached somewhere on their side.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


def _their_energy(board, player_id):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return []
    return [p for p in board.pokemon_in_play(opponent)
            if board.attached_energies(p)]


def _plumeria_playable(board, player_id, card=None):
    """2 cards to pay with, and something of theirs carrying Energy."""
    hand = board.find_player_area(player_id, "hand")
    payable = sum(1 for c in (hand.children if hand else []) if c is not card)
    return payable >= 2 and bool(_their_energy(board, player_id))


async def plumeria(ctx):
    """Pay 2 from hand, then strip an Energy off one of their Pokemon."""
    if len(await ctx.discard_from_hand(
            2, prompt="Discard 2 cards for Plumeria")) < 2:
        return
    targets = _their_energy(ctx.board, ctx.player_id)
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose one of your opponent's Pokémon to discard Energy from")
    if target is None:
        return
    energies = ctx.attached_energies(target)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose an Energy to discard.")
    if picks:
        await ctx.discard_cards(picks)


card = SupporterCardDef(
    guid="7e7a2fc9-0a3a-58ea-b22d-597474a62de7",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Plumeria.Name",
    display_name="Plumeria",
    searchable_by=["Plumeria", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=plumeria,
    condition=_plumeria_playable,
)
