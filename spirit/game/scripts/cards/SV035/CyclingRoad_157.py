"""Cycling Road (SV035 157 -- JP SV2a 165; English MEW/157). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef

from spirit.game.card_effects.trainers import is_basic_energy_card

from spirit.game.data_utils import Ability, Activations


def _cycling_condition(board, player_id, card=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_basic_energy_card(c) for c in hand.children)


async def cycling_road(ctx):
    paid = await ctx.discard_from_hand(1, minimum=1, predicate=is_basic_energy_card, prompt="Discard a Basic Energy card")
    if paid:
        await ctx.draw_cards(1)


card = StadiumCardDef(
    guid="b677ef48-2a71-590c-ad81-a34ee977de1d",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CyclingRoad.Name",
    display_name="Cycling Road",
    searchable_by=["Cycling Road", "Stadium"],
    subtypes=["Stadium"],
    collector_number=157,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Cycling Road",
        game_text="Once during each player's turn, that player may discard a Basic Energy card from their hand in order to draw a card.",
        activation=Activations.ONCE_PER_TURN,
        effect=cycling_road,
        condition=_cycling_condition,
    ),
)
