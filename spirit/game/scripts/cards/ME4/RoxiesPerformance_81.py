"""Roxie's Performance (ME - Chaos Rising 81 -- JP M4 077).

Supporter.

  "During your opponent's next turn, their Poisoned Pokemon can't retreat.
   (This includes newly Poisoned Pokemon.)"

A player-level passive (add_game_passive) that switches itself on only for
the opponent's next turn, so it doesn't depend on any Pokemon staying put
and covers Pokemon Poisoned after it was played.
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.data_utils import SupporterCardDef
from spirit.game.models.board import board_of
from spirit.game.session.passives import Passive


class RoxiesPerformancePassive(Passive):
    def __init__(self, owner_id, turn):
        self.owner_id = owner_id
        self.turn = turn

    def blocks_retreat(self, pokemon, carrier):
        if pokemon.owning_player_id == self.owner_id:
            return False
        board = board_of(pokemon)
        turn_state = getattr(board, "turn_state", None) if board is not None else None
        if turn_state is None or turn_state.turn_number != self.turn:
            return False
        return "Poisoned" in (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def roxies_performance(ctx):
    ctx.add_game_passive(RoxiesPerformancePassive(
        ctx.player_id, ctx.session.turn_state.turn_number + 1))


card = SupporterCardDef(
    guid="bd9da579-e49e-5995-af6f-9802361edae0",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoxiesPerformance.Name",
    display_name="Roxie's Performance",
    searchable_by=["Roxie's Performance", "Supporter", "RoxiesPerformance"],
    subtypes=["Supporter"],
    collector_number=81,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=roxies_performance,
)
