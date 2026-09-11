"""Heat Factory {*} (SM - Lost Thunder 178/214 -- JP SM8 081/095).

Stadium, Prism Star.

  "Once during each player's turn, that player may discard a Fire Energy
   card from their hand. If they do, they draw 3 cards."
  "Whenever any player plays an Item or Supporter card from their hand,
   prevent all effects of that card done to this Stadium card."

Scorched Earth's draw with a bigger payout and a narrower price ([R]
only), plus the Prism Star shield every one of these Stadiums prints --
ShieldedStadiumPassive, shared with Thunder Mountain and Wondrous
Labyrinth. Prism Star's own rules (one per name, Lost Zone instead of the
discard) come from the subtype and need nothing here.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import (discard_then_draw,
                                                      requires_hand)
from spirit.game.card_effects.trainers import (ShieldedStadiumPassive,
                                               is_fire_energy_card)
from spirit.game.data_utils import Ability, Activations, StadiumCardDef

ABILITY = Ability(
    title="Heat Factory",
    game_text="Once during each player's turn, that player may discard a Fire Energy card from their hand. If they do, they draw 3 cards.",
    activation=Activations.ONCE_PER_TURN,
    effect=discard_then_draw(
        1, 3, optional=False, predicate=is_fire_energy_card,
        prompt="Choose a Fire Energy card to discard."),
    condition=requires_hand(is_fire_energy_card, 1),
)

card = StadiumCardDef(
    passive=ShieldedStadiumPassive(),
    guid="e79a130a-b145-54fc-8e07-fbd4d5230d79",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeatFactoryPrismStar.Name",
    display_name="Heat Factory {*}",
    searchable_by=["Heat Factory", "Stadium", "Prism Star", "HeatFactory"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=178,
    set_code="SM8",
    rarity=Rarities.Prism,
    ability=ABILITY,
)
