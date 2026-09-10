"""Faba (SM - Lost Thunder 173/214).

Supporter.

  "Choose a Pokemon Tool or Special Energy card attached to 1 of your
   opponent's Pokemon, or any Stadium card in play, and put it in the Lost
   Zone."

One pick over three pools at once: their attached Tools, their attached
Special Energy, and the Stadium -- whoever played it, since the text says
"any Stadium card in play". Nothing attached on your own side is a target.

The Lost Zone, not the discard: what Faba takes is gone for the game.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_tool, is_special_energy


def _faba_targets(board, player_id):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    targets = []
    if opponent is not None:
        for pokemon in board.pokemon_in_play(opponent):
            targets.extend(c for c in pokemon.children
                           if is_pokemon_tool(c) or is_special_energy(c))
    stadium_area = board.find_global_area("activeStadium")
    targets.extend(stadium_area.children if stadium_area else [])
    return targets


def _faba_playable(board, player_id, card=None):
    return bool(_faba_targets(board, player_id))


async def faba(ctx):
    """Lose one of their Tools or Special Energy, or the Stadium."""
    targets = _faba_targets(ctx.board, ctx.player_id)
    if not targets:
        return
    picks = await ctx.choose_cards(
        targets, 1, prompt="Choose a card to put in the Lost Zone.")
    if picks:
        await ctx.move_to_lost_zone(picks)


card = SupporterCardDef(
    guid="3dcf4928-f018-5b8a-9e71-b4d230e59296",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Faba.Name",
    display_name="Faba",
    searchable_by=["Faba", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=faba,
    condition=_faba_playable,
)
