"""Detective Yoshida (SMPJ 25 -- JP SMP2 025; English Japan only). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def detective_yoshida(ctx):
    """Look at your opponent's hand. Draw 2 cards."""
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="127f46a7-5836-5942-9a5a-044d3bc0d4ea",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DetectiveYoshida.Name",
    display_name="Detective Yoshida",
    searchable_by=["Detective Yoshida", "Supporter"],
    subtypes=["Supporter"],
    collector_number=25,
    set_code="SMPJ",
    regulation_mark="C",
    rarity=Rarities.RarePromo,
    effect=detective_yoshida,
)
