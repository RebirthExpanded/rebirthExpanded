"""Energy Sticker (SV035 159 -- JP SV2a 152; English MEW/159). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.card_effects.trainers import is_basic_energy_card


async def energy_sticker(ctx):
    results = await ctx.flip_coins(1, "Energy Sticker")
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not (results and results[0]) or not bench or not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Energy card to attach")
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon") if picks else None
    if target is not None:
        await ctx.attach_energy(picks[0], target)


card = ItemCardDef(
    guid="0a726844-ebf9-563b-ade4-2f6d9228c90e",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySticker.Name",
    display_name="Energy Sticker",
    searchable_by=["Energy Sticker", "Item"],
    subtypes=["Item"],
    collector_number=159,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=energy_sticker,
)
