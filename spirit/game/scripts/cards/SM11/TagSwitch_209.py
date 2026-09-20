"""Tag Switch (SM - Unified Minds 209/236 -- JP SM10a 045/054, the art here).

Item.

  "Move up to 2 Energy from 1 of your TAG TEAM Pokemon to another of
   your Pokemon."

One source (a TAG TEAM with Energy), one destination (any other Pokemon
of yours), then up to 2 of the source's Energy in one pick. Playable
only with such a source and a second Pokemon in play.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef, subtypes_for

MAX_MOVED = 2


def _is_tag_team_pokemon(pokemon) -> bool:
    return "TAG TEAM" in subtypes_for(pokemon.archetype_id)


def _tag_switch_playable(board, player_id) -> bool:
    in_play = board.pokemon_in_play(player_id)
    return len(in_play) >= 2 and any(
        _is_tag_team_pokemon(p) and board.attached_energies(p) for p in in_play)


async def tag_switch(ctx):
    in_play = ctx.my_pokemon_in_play()
    sources = [p for p in in_play if _is_tag_team_pokemon(p) and ctx.attached_energies(p)]
    if not sources or len(in_play) < 2:
        return
    source = await ctx.choose_pokemon(
        sources, "Choose a TAG TEAM Pokémon to move Energy from")
    if source is None:
        return
    dest = await ctx.choose_pokemon(
        [p for p in in_play if p is not source], "Choose a Pokémon to move the Energy to")
    if dest is None:
        return
    pool = ctx.attached_energies(source)
    picks = await ctx.choose_cards(
        pool, min(MAX_MOVED, len(pool)), minimum=1,
        prompt="Choose up to 2 Energy to move")
    for energy in picks:
        await ctx.move_energy(energy, dest)


card = ItemCardDef(
    guid="6f1685cc-67e8-5b08-a271-a3c7a7c08f3d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TagSwitch.Name",
    display_name="Tag Switch",
    searchable_by=["Tag Switch", "Item", "TagSwitch"],
    subtypes=["Item"],
    collector_number=209,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    condition=_tag_switch_playable,
    effect=tag_switch,
)
