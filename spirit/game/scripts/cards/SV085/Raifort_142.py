"""Raifort (SV085 142 -- JP SV8a 199; English PRE/142, TWM/161). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def raifort(ctx):
    top = list(ctx.deck_top(5))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    picks = await ctx.choose_cards(top, len(top), minimum=0, prompt="Discard any number of these cards")
    if picks:
        await ctx.discard_cards(picks)
    left = len(top) - len(picks)
    if left > 1:
        await ctx.reorder_deck_top(left)


card = SupporterCardDef(
    guid="29f01bfc-a796-582d-9e3a-a01f25b3f680",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Raifort.Name",
    display_name="Raifort",
    searchable_by=["Raifort", "Supporter"],
    subtypes=["Supporter"],
    collector_number=142,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareUltra,
    effect=raifort,
)
