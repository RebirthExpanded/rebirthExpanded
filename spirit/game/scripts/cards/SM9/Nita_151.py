"""Nita (SM - Team Up 151/181 -- JP SM8b 140/150, the art here).

Supporter.

  "You can play this card only if your opponent's Active Pokemon is a
   Basic Pokemon."
  "Put an Energy attached to your opponent's Active Pokemon on top of
   their deck."

Team Star Grunt's effect behind the sisters' Stage gate; with no Energy
on their Active there is nothing to move, so the card is not offered.
"""

from spirit.game.attributes import PokemonStage, Rarities
from spirit.game.card_effects.trainers import (is_energy_card,
                                               opponent_active_is_stage)
from spirit.game.data_utils import SupporterCardDef

_basic_active = opponent_active_is_stage(PokemonStage.BASIC)


def _active_energies(board, player_id):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    active = board.active_pokemon(opponent) if opponent else None
    return [c for c in (active.children if active else []) if is_energy_card(c)]


def _playable(board, player_id, card=None) -> bool:
    return _basic_active(board, player_id) and bool(_active_energies(board, player_id))


async def nita(ctx):
    targets = _active_energies(ctx.board, ctx.player_id)
    if not targets:
        return
    picks = await ctx.choose_cards(
        targets, 1, minimum=1,
        prompt="Choose an Energy to put on top of your opponent's deck")
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = SupporterCardDef(
    guid="8974ad88-798f-515e-9a8b-f93535b88ccf",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nita.Name",
    display_name="Nita",
    searchable_by=["Nita", "Supporter"],
    subtypes=["Supporter"],
    collector_number=151,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    condition=_playable,
    effect=nita,
)
