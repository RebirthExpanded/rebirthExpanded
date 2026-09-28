"""Energy Swatter (ME - Perfect Order 73 -- JP M3 067).

Item.

  "Your opponent reveals their hand, and you choose an Energy card you find
   there and put it on the bottom of their deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_energy_card


def _opponent_has_hand(board, player_id, card=None) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    hand = board.find_player_area(opponent, "hand") if opponent else None
    return bool(hand and hand.children)


async def energy_swatter(ctx):
    opp = ctx.opponent_id
    hand = await ctx.reveal_hand(opp)
    energies = [c for c in hand if is_energy_card(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(energies, 1, prompt="Choose an Energy card to put on the bottom of their deck")
    if picks:
        await ctx.put_on_bottom_of_deck(picks[0])


card = ItemCardDef(
    guid="470c9507-02c0-5877-9dee-b27bc1fb10a6",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwatter.Name",
    display_name="Energy Swatter",
    searchable_by=["Energy Swatter", "Item", "EnergySwatter"],
    subtypes=["Item"],
    collector_number=73,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    condition=_opponent_has_hand,
    effect=energy_swatter,
)
