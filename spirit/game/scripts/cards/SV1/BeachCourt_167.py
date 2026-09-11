"""Beach Court (SV - Scarlet & Violet 167/198 -- JP SV1S 078/078).

Stadium.  "The Retreat Cost of each Basic Pokemon in play (both yours and
your opponent's) is [C] less."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import retreat_discount
from spirit.game.data_utils import StadiumCardDef
from spirit.game.session.effects import is_basic_pokemon_in_play

card = StadiumCardDef(
    guid="15072850-a4df-5c5e-ab73-9c897b9ca46a",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeachCourt.Name",
    display_name="Beach Court",
    searchable_by=["Beach Court", "Stadium", "BeachCourt"],
    subtypes=["Stadium"],
    collector_number=167,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    passive=retreat_discount(1, target_pred=lambda p, c: is_basic_pokemon_in_play(p)),
)
