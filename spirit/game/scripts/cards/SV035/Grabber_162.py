"""Grabber (SV035 162 -- JP SV2a 153; English MEW/162). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.session.effects import is_pokemon_card


async def grabber(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    pool = [c for c in hand if is_pokemon_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Pokémon to put on the bottom of their deck")
        if picks:
            await ctx.put_on_bottom_of_deck(picks[0])


card = ItemCardDef(
    guid="6fe98924-7621-58de-a937-88086c0a6864",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grabber.Name",
    display_name="Grabber",
    searchable_by=["Grabber", "Item"],
    subtypes=["Item"],
    collector_number=162,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=grabber,
)
