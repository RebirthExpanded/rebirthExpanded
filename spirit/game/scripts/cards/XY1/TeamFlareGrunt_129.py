"""Team Flare Grunt (XY 129/146 -- JP XY1-Bx 060/060).

Supporter.

  "Discard an Energy attached to your opponent's Active Pokemon."

Not offered with nothing to discard: the Active has to have an Energy on
it. The choice of which one is yours.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef


def _their_active_has_energy(board, player_id) -> bool:
    opponent = next((p for p in board.player_ids if p != player_id), None)
    active = board.active_pokemon(opponent) if opponent else None
    return active is not None and bool(board.attached_energies(active))


async def team_flare_grunt(ctx):
    active = ctx.opponent_active()
    if active is None:
        return
    await ctx.discard_energy_from(
        active, 1, prompt="Choose an Energy to discard from the Active Pokémon")


card = SupporterCardDef(
    guid="f50b5b73-5167-540a-800f-83526a5a0626",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamFlareGrunt.Name",
    display_name="Team Flare Grunt",
    searchable_by=["Team Flare Grunt", "Supporter", "TeamFlareGrunt"],
    subtypes=["Supporter"],
    collector_number=129,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=team_flare_grunt,
    condition=_their_active_has_energy,
)
