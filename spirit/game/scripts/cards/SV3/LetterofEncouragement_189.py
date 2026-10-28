"""Letter of Encouragement (SV3 189 -- JP SV3 100; English OBF/189). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card



def _lost_last_turn(board, player_id, card=None) -> bool:
    ts = getattr(board, "turn_state", None)
    return ts is not None and bool(ts.kos_suffered_last_turn.get(player_id))


card = ItemCardDef(
    guid="0c2c8304-94ab-515c-9791-6d738618d0c0",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LetterofEncouragement.Name",
    display_name="Letter of Encouragement",
    searchable_by=["Letter of Encouragement", "Item"],
    subtypes=["Item"],
    collector_number=189,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_lost_last_turn,
    effect=su.search_to_hand(is_basic_energy_card, count=3, reveal=True, prompt="Choose up to 3 Basic Energy cards."),
)
