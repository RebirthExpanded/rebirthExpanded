"""Team Rocket's Harassment (ロケット団のいやがらせ -- JP SM-D 026; no
English print, pool slot Promo_SM 902).

Supporter.

  "Each player shuffles their hand into their deck. Then, each player
   draws 5 cards."

Judge with 5 for both sides.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="3ce16595-63fb-58ad-8cd6-2712d027271f",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsHarassment.Name",
    display_name="Team Rocket's Harassment",
    searchable_by=["Team Rocket's Harassment", "Supporter", "TeamRocketsHarassment"],
    subtypes=["Supporter"],
    collector_number=902,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    effect=shuffle_hand_into_deck_draw(5, opponent_n=5),
)
