"""Granite Cave (SV10 166 -- JP SVOD 018; English DRI/166). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef

from spirit.game.card_effects import passives_common as pc
from spirit.game.data_utils import def_for, subtypes_for


def _named(prefix):
    def pred(card) -> bool:
        return card is not None and (getattr(def_for(card.archetype_id), "display_name", "") or "").startswith(prefix)
    return pred


def _name_has(*parts):
    def pred(card) -> bool:
        name = (getattr(def_for(card.archetype_id), "display_name", "") or "") if card is not None else ""
        return any(p in name for p in parts)
    return pred


card = StadiumCardDef(
    guid="f017099b-f527-5a61-8347-359e83ba467e",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GraniteCave.Name",
    display_name="Granite Cave",
    searchable_by=["Granite Cave", "Stadium"],
    subtypes=["Stadium"],
    collector_number=166,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=pc.takes_less_passive(30, protects=lambda target, carrier: _named("Steven's ")(target)),
)
