"""Dana (SM - Team Up 137/181 -- JP SM8b 138/150, the art here).

Supporter.

  "You can play this card only if your opponent's Active Pokemon is a
   Stage 2 Pokemon."
  "Search your deck for up to 2 cards and put them into your hand. Then,
   shuffle your deck."

One of the four sisters (Morgan, Dana, Evelyn, Nita); each is gated on
what their opponent has in the Active Spot, read live from the printed
Stage.
"""

from spirit.game.attributes import PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import opponent_active_is_stage
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="72df36ae-549f-563e-9a1b-ac27a2084930",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dana.Name",
    display_name="Dana",
    searchable_by=["Dana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    condition=opponent_active_is_stage(PokemonStage.STAGE2),
    effect=search_to_hand(None, count=2, minimum=0, reveal=False,
                          prompt="Choose up to 2 cards to put into your hand."),
)
