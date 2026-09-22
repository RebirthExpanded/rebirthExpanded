"""Team Star Grunt (SV - Scarlet & Violet 195/198 -- JP SV1S 075/078, the art here).

Supporter.

  "Put an Energy attached to your opponent's Active Pokemon on top of
   their deck."

Team Yell Grunt aimed at the Active alone, and the Energy goes on their
deck rather than into their hand.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.data_utils import SupporterCardDef


def _active_energies(board, player_id):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    active = board.active_pokemon(opponent) if opponent else None
    return [c for c in (active.children if active else []) if is_energy_card(c)]


def _opponent_active_has_energy(board, player_id) -> bool:
    return bool(_active_energies(board, player_id))


async def team_star_grunt(ctx):
    targets = _active_energies(ctx.board, ctx.player_id)
    if not targets:
        return
    picks = await ctx.choose_cards(
        targets, 1, minimum=1,
        prompt="Choose an Energy to put on top of your opponent's deck")
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = SupporterCardDef(
    guid="40076b3f-beda-5a86-bc8e-59252be6f59e",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamStarGrunt.Name",
    display_name="Team Star Grunt",
    searchable_by=["Team Star Grunt", "Supporter", "TeamStarGrunt"],
    subtypes=["Supporter"],
    collector_number=195,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_opponent_active_has_energy,
    effect=team_star_grunt,
)
