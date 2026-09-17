"""Cassius (XY - Flashfire 115/106 -- JP XY1 058/060, the art here).

Supporter.

  "Shuffle 1 of your Pokemon and all cards attached to it into your deck."

AZ with the deck for a destination: the whole stack -- the Pokemon, its
pre-evolutions, Energy, Tools -- goes into the deck and the damage on it
is gone with it (Q&A). Any of your Pokemon may be chosen, the Active
included; then a new Active is promoted after the choreography lands, and
a player whose only Pokemon this was loses the game (Q&A: playable with
one Pokemon in play).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import full_stack


async def cassius(ctx):
    """One of your Pokemon and everything under it, into the deck."""
    mine = ctx.my_pokemon_in_play()
    if not mine:
        return
    target = await ctx.choose_pokemon(
        mine, "Choose 1 of your Pokémon to shuffle into your deck.")
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.shuffle_into_deck(full_stack(target), ctx.player_id)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


def _cassius_playable(board, player_id) -> bool:
    return bool(board.pokemon_in_play(player_id))


card = SupporterCardDef(
    guid="8008b229-4623-5dc3-9915-35d33116407e",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cassius.Name",
    display_name="Cassius",
    searchable_by=["Cassius", "Supporter"],
    subtypes=["Supporter"],
    collector_number=115,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    condition=_cassius_playable,
    effect=cassius,
)
