"""Iris's Fighting Spirit (SV09 149 -- JP SV9 094; English ASC/190, ASC/292, JTG/149, JTG/180). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

def _another_card(board, player_id, card=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len([c for c in hand.children if c is not card]) >= 1


async def iris_fighting_spirit(ctx):
    paid = await ctx.discard_from_hand(1, minimum=1, exclude=[ctx.source],
                                       prompt="Discard a card from your hand to use Iris's Fighting Spirit.")
    if paid:
        await ctx.draw_until(6)


card = SupporterCardDef(
    guid="54b22b9c-6a7b-5858-8286-1758c4c4f559",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IrissFightingSpirit.Name",
    display_name="Iris's Fighting Spirit",
    searchable_by=["Iris's Fighting Spirit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=_another_card,
    effect=iris_fighting_spirit,
)
