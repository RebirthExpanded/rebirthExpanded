"""Atticus (SV - Paldean Fates 77/91 -- JP SV-P 056, the art here).

Supporter.

  "You can use this card only if your opponent's Active Pokemon is
   Poisoned. Shuffle your hand into your deck. Then, draw 7 cards."
"""

from spirit.game.attributes import (
    CLIENT_SPECIAL_CONDITION_NAMES, AttrID, Rarities, SpecialConditions,
)
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw
from spirit.game.data_utils import SupporterCardDef

_POISONED = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]


def _opponent_active_poisoned(board, player_id, card=None) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    active = board.active_pokemon(opponent) if opponent is not None else None
    return active is not None and \
        _POISONED in (active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


card = SupporterCardDef(
    guid="f3dc9295-6571-5205-92b0-d1c95a480022",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Atticus.Name",
    display_name="Atticus",
    searchable_by=["Atticus", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_opponent_active_poisoned,
    effect=shuffle_hand_into_deck_draw(7),
)
