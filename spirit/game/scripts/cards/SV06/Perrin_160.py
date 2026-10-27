"""Perrin (SV06 160 -- JP SV5a 063; English TWM/160, TWM/209, TWM/220). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.session.effects import is_pokemon_card


async def perrin(ctx):
    pool = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Reveal up to 2 Pokémon to put into your deck")
    if not picks:
        return
    await ctx.reveal_cards(picks)
    await ctx.shuffle_into_deck(picks, ctx.player_id)
    found = await ctx.search_deck(is_pokemon_card, count=len(picks), minimum=0,
                                  prompt=f"Choose up to {len(picks)} Pokémon to put into your hand.")
    if found:
        await ctx.put_in_hand(found)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="124134e9-0e31-5d34-8495-9d22d4675741",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Perrin.Name",
    display_name="Perrin",
    searchable_by=["Perrin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=160,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=perrin,
)
