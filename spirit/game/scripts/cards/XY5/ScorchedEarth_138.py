"""Scorched Earth (XY - Primal Clash 138/160 -- JP XY5-Bg 068/070).

Stadium.

  "Once during each player's turn, that player may discard a Fire or Fighting Energy card from their hand. If that player does so, they draw 2 cards."

Offered only with an [R] or [F] Energy card in hand; the discard is
the price of the draw.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import (discard_then_draw,
                                                      requires_hand)
from spirit.game.card_effects.trainers import is_fire_or_fighting_energy_card
from spirit.game.data_utils import Ability, Activations, StadiumCardDef

ABILITY = Ability(
    title="Scorched Earth",
    game_text="Once during each player's turn, that player may discard a Fire or Fighting Energy card from their hand. If that player does so, they draw 2 cards.",
    activation=Activations.ONCE_PER_TURN,
    effect=discard_then_draw(
        1, 2, optional=False, predicate=is_fire_or_fighting_energy_card,
        prompt="Choose a Fire or Fighting Energy card to discard."),
    condition=requires_hand(is_fire_or_fighting_energy_card, 1),
)

card = StadiumCardDef(
    guid="cb14f786-a063-5fe5-90b9-a1fc9d9bf539",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScorchedEarth.Name",
    display_name="Scorched Earth",
    searchable_by=["Scorched Earth", "Stadium", "ScorchedEarth"],
    subtypes=["Stadium"],
    collector_number=138,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    ability=ABILITY,
)
