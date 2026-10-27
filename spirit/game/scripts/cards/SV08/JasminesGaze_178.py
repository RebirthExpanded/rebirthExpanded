"""Jasmine's Gaze (SV08 178 -- JP SV8 104; English SSP/178, SSP/233, SSP/245). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.session.passives import Passive


class _JasminesGaze(Passive):
    """Game-level: during that turn, the owner's Pokemon take 30 less from
    the opponent's attacks (after W/R)."""

    def __init__(self, owner, turn):
        self.owner, self.turn = owner, turn

    def modify_damage_taken(self, calc, carrier):
        ts = getattr(calc.board, "turn_state", None)
        if (ts is not None and ts.turn_number == self.turn and calc.is_attack and calc.is_opposing
                and calc.target.owning_player_id == self.owner):
            calc.amount = max(0, calc.amount - 30)


async def jasmines_gaze(ctx):
    ctx.add_game_passive(_JasminesGaze(ctx.player_id, ctx.session.turn_state.turn_number + 1))


card = SupporterCardDef(
    guid="cca50037-0615-508f-b407-a13ff61b1718",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JasminesGaze.Name",
    display_name="Jasmine's Gaze",
    searchable_by=["Jasmine's Gaze", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=jasmines_gaze,
)
