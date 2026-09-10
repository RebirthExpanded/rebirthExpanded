"""Super Scoop Up (SM - Celestial Storm 146/168 -- JP SM6b 054/066).

Item.

  "Flip a coin. If heads, put 1 of your Pokemon and all cards attached to
   it into your hand."

The whole stack comes back: the Pokemon card, everything under it and
everything attached. Taking the Active back empties the Active spot, so a
Benched Pokemon is promoted afterwards -- and with no Bench to promote
from, the game is lost, which is the risk the card carries.

The coin is flipped before anything is chosen, so tails costs the Item and
nothing else.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import full_stack


async def scoop_up(ctx):
    """One of your Pokemon and everything on it, back to hand."""
    candidates = ctx.my_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your Pokémon to put into your hand.")
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.put_in_hand(full_stack(target), reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


card = ItemCardDef(
    guid="f5d2eebb-93c6-5e1d-9956-c022fe82882d",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item", "SuperScoopUp"],
    subtypes=["Item"],
    collector_number=146,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=flip_or_nothing(then=scoop_up),
)
