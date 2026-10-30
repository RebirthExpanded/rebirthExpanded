from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import full_stack


async def super_scoop_up(ctx):
    """Flip a coin. If heads, put 1 of your Pokemon and all cards attached to
    it into your hand."""
    if not (await ctx.flip_coins(1, "Super Scoop Up"))[0]:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(),
        "Choose 1 of your Pokémon to put into your hand",
    )
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.put_in_hand(full_stack(target), reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


card = ItemCardDef(
    guid="d9469aa4-6859-537a-9dae-50ca13a6f394",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=124,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=super_scoop_up,
)
