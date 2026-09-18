"""Lana's Fishing Rod (SM - Cosmic Eclipse 195/236 -- JP SM11b 042/049, the
art here).

Item.

  "Shuffle a Pokemon and a Pokemon Tool card from your discard pile into
   your deck."

Playable with either kind in the discard pile; each is chosen from its own
list (or taken automatically when only one qualifies), and both go back
in one shuffle. The JP print adds "reveal them", so the picks are shown
to the opponent before they fly.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_pokemon_card, is_pokemon_tool


def _lanas_fishing_rod_playable(board, player_id) -> bool:
    area = board.find_player_area(player_id, "discard")
    return any(is_pokemon_card(c) or is_pokemon_tool(c) for c in (area.children if area else []))


async def lanas_fishing_rod(ctx):
    picks = []
    for predicate, what in ((is_pokemon_card, "Pokémon"), (is_pokemon_tool, "Pokémon Tool")):
        pool = [c for c in ctx.discard_pile() if predicate(c)]
        if not pool:
            continue
        if len(pool) == 1:
            picks.extend(pool)
            continue
        picks.extend(await ctx.choose_cards(
            pool, 1, minimum=1, prompt=f"Choose a {what} card to shuffle into your deck."))
    if not picks:
        return
    await ctx.reveal_cards(picks, to_player=ctx.opponent_id)
    await ctx.shuffle_into_deck(picks)


card = ItemCardDef(
    guid="5db00387-db51-58da-84fc-150b7e1d92e8",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanasFishingRod.Name",
    display_name="Lana's Fishing Rod",
    searchable_by=["Lana's Fishing Rod", "Item", "LanasFishingRod"],
    subtypes=["Item"],
    collector_number=195,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    condition=_lanas_fishing_rod_playable,
    effect=lanas_fishing_rod,
)
