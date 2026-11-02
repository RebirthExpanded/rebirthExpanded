"""Abareru-kun (SMPJ 320 -- JP SMP 320; English Japan only). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def abareru_kun(ctx):
    """Tell your opponent a joke. If they laugh, draw 3 cards. An AI
    opponent laughs at random."""
    import random
    from spirit.game.session.ai_player import AIPlayer

    if isinstance(ctx.session.players.get(ctx.opponent_id), AIPlayer):
        laughed = random.random() < 0.5
    else:
        laughed = await ctx.choose("Your opponent told you a joke. Did you laugh?", ["Laughed", "Didn't laugh"],
                                   player_id=ctx.opponent_id, use_panel=False) == 0
    if laughed:
        await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="7416624c-c247-55ff-a5b7-0dd08f114c38",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Abarerukun.Name",
    display_name="Abareru-kun",
    searchable_by=["Abareru-kun", "Supporter"],
    subtypes=["Supporter"],
    collector_number=320,
    set_code="SMPJ",
    regulation_mark="C",
    rarity=Rarities.RarePromo,
    effect=abareru_kun,
)
