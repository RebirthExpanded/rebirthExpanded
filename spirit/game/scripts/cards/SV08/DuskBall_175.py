"""Dusk Ball (SV08 175 -- JP SV7a 054; English MD/80, MT/110, SSP/175). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.session.effects import is_pokemon_card


async def dusk_ball(ctx):
    deck = list(ctx.deck())
    bottom = deck[-7:] if deck else []
    if not bottom:
        return
    await ctx.reveal_cards(bottom, to_player=ctx.player_id)
    pool = [c for c in bottom if is_pokemon_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="You may put a Pokémon into your hand")
        if picks:
            await ctx.put_in_hand(picks)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="af6502e1-f4ed-558c-9a47-54c40a847bd3",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskBall.Name",
    display_name="Dusk Ball",
    searchable_by=["Dusk Ball", "Item"],
    subtypes=["Item"],
    collector_number=175,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=dusk_ball,
)
