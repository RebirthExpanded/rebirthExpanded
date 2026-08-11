from spirit.game.card_effects.trainers import opponent_has_bench
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def prime_catcher(ctx):
    """Switch in 1 of your opponent's Benched Pokémon. If you do, switch
    your Active with 1 of your Benched Pokémon."""
    target = await ctx.choose_pokemon(
        ctx.opponent_bench(), "Choose the opponent's new Active Pokémon"
    )
    if target is None:
        return
    await ctx.switch_active(ctx.opponent_id, target)
    my_bench = ctx.my_bench()
    if not my_bench:
        return
    mine = await ctx.choose_pokemon(
        my_bench, "Choose your new Active Pokémon"
    )
    if mine is not None:
        await ctx.switch_active(ctx.player_id, mine)


card = ItemCardDef(
    guid="b6707998-5001-51da-8fc1-0eccbbe1fde8",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PrimeCatcher.Name",
    display_name="Prime Catcher",
    searchable_by=["Prime Catcher", "Item", "ACE SPEC", "PrimeCatcher"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=157,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareUltra,
    effect=prime_catcher,
    condition=opponent_has_bench,
)
