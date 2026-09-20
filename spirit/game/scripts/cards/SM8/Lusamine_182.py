"""Lusamine {*} (SM - Lost Thunder 182/214 -- JP SM8 092/095, the art here).

Supporter, Prism Star.

  "You can play this card only if your opponent has exactly 3 Prize cards
   remaining. During your opponent's next turn, prevent all damage done to
   your Ultra Beasts by attacks from your opponent's Pokemon."

The shield belongs to the player, not to a Pokemon: an Ultra Beast put
onto the Bench later this turn is covered too, and it survives the
Active leaving. It is a game passive (Full Metal Wall-GX's shape) that
answers only through the opponent's next turn and goes quiet after.
Prism Star: one per deck, to the Lost Zone after use.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import prizes_remaining
from spirit.game.card_effects.trainers import is_ultra_beast
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.passives import Passive


class LusamineShieldPassive(Passive):
    """Opposing attacks do no damage to `owner_id`'s Ultra Beasts through `expires_after_turn`."""

    def __init__(self, owner_id: str, expires_after_turn: int):
        self.owner_id = owner_id
        self.expires_after_turn = expires_after_turn

    def _live(self, board) -> bool:
        state = getattr(board, "turn_state", None)
        return state is not None and state.turn_number <= self.expires_after_turn

    def prevents_damage(self, calc, carrier):
        target = calc.target
        return bool(
            calc.is_attack and calc.is_opposing and target is not None
            and target.owning_player_id == self.owner_id
            and is_ultra_beast(target) and self._live(calc.board))


def _lusamine_prism_condition(board, player_id) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    return opponent is not None and prizes_remaining(board, opponent) == 3


async def lusamine_prism_star(ctx):
    ctx.add_game_passive(LusamineShieldPassive(
        ctx.player_id, ctx.session.turn_state.turn_number + 1))


card = SupporterCardDef(
    guid="c9b244fe-0f73-5761-84f7-3128b605710a",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LusaminePrismStar.Name",
    display_name="Lusamine {*}",
    searchable_by=["Lusamine", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=182,
    set_code="SM8",
    rarity=Rarities.Prism,
    condition=_lusamine_prism_condition,
    effect=lusamine_prism_star,
)
