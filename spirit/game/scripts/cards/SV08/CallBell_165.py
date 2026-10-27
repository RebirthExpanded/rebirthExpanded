"""Call Bell (SV08 165 -- JP SV7a 053; English SSP/165). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.card_effects import support_common as su

from spirit.game.card_effects.trainers import second_players_first_turn
from spirit.game.session.effects import is_supporter_card


card = ItemCardDef(
    guid="3ab9e020-b708-5a7d-813c-643db2f28f70",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CallBell.Name",
    display_name="Call Bell",
    searchable_by=["Call Bell", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=second_players_first_turn,
    effect=su.search_to_hand(is_supporter_card, count=1, reveal=True, prompt="Choose a Supporter card."),
)
