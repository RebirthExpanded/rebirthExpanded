"""Teammates (XY - Primal Clash 141/160 -- JP XY5 066/070, the art here).

Supporter.

  "You can play this card only if 1 of your Pokemon was Knocked Out
   during your opponent's last turn."
  "Search your deck for up to 2 cards and put them into your hand.
   Shuffle your deck afterward."

The revenge clause is Rosa's (ally_ko_last_turn), which skips knockouts
that happened at the Pokemon Checkup (pool ruling).
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import ally_ko_last_turn
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="3875012a-400e-5d1d-bc22-08eb54aeba83",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Teammates.Name",
    display_name="Teammates",
    searchable_by=["Teammates", "Supporter"],
    subtypes=["Supporter"],
    collector_number=141,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    condition=ally_ko_last_turn,
    effect=search_to_hand(None, count=2, minimum=0, reveal=False,
                          prompt="Choose up to 2 cards to put into your hand."),
)
