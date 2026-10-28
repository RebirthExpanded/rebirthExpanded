"""Rika (SV4 172 -- JP SV3a 060; English PAR/172, PAR/241, PAR/258). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def rika(ctx):
    top = list(ctx.deck_top(4))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    picks = await ctx.choose_cards(top, min(2, len(top)), minimum=min(2, len(top)), prompt="Choose 2 cards to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    rest = [c for c in top if c not in picks]
    import random
    random.shuffle(rest)
    for card in rest:
        await ctx.put_on_bottom_of_deck(card)


card = SupporterCardDef(
    guid="9a218c5d-39f4-503a-a4e7-360ac0306dc2",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rika.Name",
    display_name="Rika",
    searchable_by=["Rika", "Supporter"],
    subtypes=["Supporter"],
    collector_number=172,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=rika,
)
