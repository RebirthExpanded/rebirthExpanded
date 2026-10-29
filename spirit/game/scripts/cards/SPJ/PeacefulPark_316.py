"""Peaceful Park (SPJ 316 -- JP SP 316; English Japan only). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef

from spirit.game.attributes import SpecialConditions
from spirit.game.data_utils import Ability, Triggers
from spirit.game.session.passives import Passive


class _PeacefulPark(Passive):
    def blocks_special_conditions(self, target, condition, carrier):
        return condition == SpecialConditions.CONFUSED


async def _peaceful_park_played(ctx):
    for pid in (ctx.player_id, ctx.opponent_id):
        for p in ctx.board.pokemon_in_play(pid):
            await ctx.cure_condition(p, SpecialConditions.CONFUSED)


card = StadiumCardDef(
    guid="005c4af0-a59e-5d89-b459-f1e598618dd7",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PeacefulPark.Name",
    display_name="Peaceful Park",
    searchable_by=["Peaceful Park", "Stadium"],
    subtypes=["Stadium"],
    collector_number=316,
    set_code="SPJ",
    regulation_mark="F",
    rarity=Rarities.RarePromo,
    passive=_PeacefulPark(),
    abilities=[
        Ability(
            title="Peaceful Park",
            game_text="Pokémon in play can't be Confused. If a Pokémon in play is already Confused, remove that Special Condition.",
            trigger=Triggers.ON_PLAY,
            effect=_peaceful_park_played,
        ),
    ],
)
