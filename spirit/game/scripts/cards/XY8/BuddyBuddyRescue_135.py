"""Buddy-Buddy Rescue (XY - BREAKthrough 135/162 -- JP SNPr 006/016).

Item.

  "Each player puts a Pokemon from their discard pile into their hand.
   (Your opponent chooses first.)"

Both picks are mandatory where possible and revealed; the opponent
chooses first. Playable while either discard pile holds a Pokemon.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_pokemon_card


def _condition(board, player_id, pokemon=None) -> bool:
    for pid in board.player_ids:
        pile = board.find_player_area(pid, "discard")
        if pile and any(is_pokemon_card(c) for c in pile.children):
            return True
    return False


async def buddy_buddy_rescue(ctx):
    for pid in (ctx.opponent_id, ctx.player_id):
        pokemon = [c for c in ctx.discard_pile(pid) if is_pokemon_card(c)]
        if not pokemon:
            continue
        picks = await ctx.choose_cards(
            pokemon, 1, minimum=1, player_id=pid,
            prompt="Choose a Pokémon from your discard pile to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)


card = ItemCardDef(
    guid="55bfee03-eae6-5056-8198-2e3d700272cf",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BuddyBuddyRescue.Name",
    display_name="Buddy-Buddy Rescue",
    searchable_by=["Buddy-Buddy Rescue", "Item", "BuddyBuddyRescue"],
    subtypes=["Item"],
    collector_number=135,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    condition=_condition,
    effect=buddy_buddy_rescue,
)
