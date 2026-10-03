"""Megaton Blower (SV - Surging Sparks 182/191 -- JP SV7a 064/064, the art
here).

Item -- ACE SPEC.

  "Discard all Pokemon Tools and Special Energy from all of your opponent's
   Pokemon, and discard a Stadium in play."

Everything goes at once. A Pokemon that the lost HP (Bravery Charm, Lively
Stadium) leaves at 0 is Knocked Out with this card's knockouts -- after a
Bench that shrank (Area Zero Underdepths gone) has been discarded down to
size, so a Pokemon discarded there is not Knocked Out (official Q&A; the
trainer executor settles the Bench first).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import full_stack, is_pokemon_tool, is_special_energy


def _targets(board, opponent_id):
    return [c for pokemon in board.pokemon_in_play(opponent_id)
            for c in full_stack(pokemon)
            if c is not pokemon and (is_pokemon_tool(c) or is_special_energy(c))]


def _stadium_in_play(board) -> bool:
    area = board.find_global_area("activeStadium")
    return bool(area and area.children)


def _megaton_blower_playable(board, player_id) -> bool:
    opponent = next((p for p in board.player_ids if p != player_id), None)
    return _stadium_in_play(board) or bool(opponent and _targets(board, opponent))


async def megaton_blower(ctx):
    doomed = _targets(ctx.board, ctx.opponent_id)
    if doomed:
        await ctx.discard_cards(doomed)
    if _stadium_in_play(ctx.board):
        await ctx.discard_stadium()


card = ItemCardDef(
    guid="e60f6707-4361-5616-b893-e84ef10d8392",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegatonBlower.Name",
    display_name="Megaton Blower",
    searchable_by=["Megaton Blower", "Item", "ACE SPEC", "MegatonBlower"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=182,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Ace,
    condition=_megaton_blower_playable,
    effect=megaton_blower,
)
