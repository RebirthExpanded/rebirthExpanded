"""Bill's Transfer (SV035 156 -- JP SV2a 164; English MEW/156, MEW/194). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.session.effects import is_pokemon_card


async def bills_transfer(ctx):
    top = list(ctx.deck_top(8))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    pool = [c for c in top if is_pokemon_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Choose any number of Pokémon to put into your hand")
        if picks:
            await ctx.put_in_hand(picks)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="0c91261f-7a18-569a-a9f6-2836a08d8237",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsTransfer.Name",
    display_name="Bill's Transfer",
    searchable_by=["Bill's Transfer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=156,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=bills_transfer,
)
