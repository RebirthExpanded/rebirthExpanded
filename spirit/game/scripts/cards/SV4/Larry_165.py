"""Larry (SV4 165 -- JP SV3a 058; English PAR/165, PAR/235). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.session.effects import is_basic_pokemon, is_pokemon_card


async def larry(ctx):
    results = await ctx.flip_coins(1, "Larry")
    if results and results[0]:
        picks = await ctx.search_deck(is_pokemon_card, count=2, minimum=0, prompt="Choose up to 2 Pokémon.")
    else:
        picks = await ctx.search_deck(is_basic_pokemon, count=1, minimum=0, prompt="Choose a Basic Pokémon.")
    if picks:
        await ctx.put_in_hand(picks)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="bb0f4939-27b2-533f-9ed4-11bdb8fc0a66",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Larry.Name",
    display_name="Larry",
    searchable_by=["Larry", "Supporter"],
    subtypes=["Supporter"],
    collector_number=165,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    effect=larry,
)
