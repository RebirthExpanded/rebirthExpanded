"""Pokémon Enterprise (BWPJ 597 -- JP EBB 097; English Japan only). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def _enterprise(ctx):
    """Flip a coin. If heads, heal 30 damage from 1 of your Pokemon. If tails, draw 3 cards."""
    results = await ctx.flip_coins(1, "Pokémon Enterprise")
    if results and results[0]:
        from spirit.game.card_effects import support_common as su
        await su.heal_targets(30, "choice")(ctx)
    else:
        await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="c62b7d1c-2c8a-54c8-a71a-a30e4c752df7",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonEnterprise.Name",
    display_name="Pokémon Enterprise",
    searchable_by=["Pokémon Enterprise", "Supporter"],
    subtypes=["Supporter"],
    collector_number=597,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    effect=_enterprise,
)
