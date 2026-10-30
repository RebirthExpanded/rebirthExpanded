"""Choice Band (SM - Guardians Rising 121/145 -- JP SM6 084/094, the art here).

Pokemon Tool.

  "The attacks of the Pokemon this card is attached to do 30 more damage
   to your opponent's Active Pokemon-GX and Pokemon-EX (before applying
   Weakness and Resistance)."

The Gloves shape with a subtype target: Pokemon-GX and the XY-era
Pokemon-EX ("EX"), not the SV-era ex.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import typed_damage_boost_tool
from spirit.game.data_utils import PokemonToolCardDef, subtypes_for

BOOST = 30


def _gx_or_ex(target) -> bool:
    subtypes = subtypes_for(target.archetype_id)
    return "GX" in subtypes or "EX" in subtypes


card = PokemonToolCardDef(
    guid="6b20d3a2-dbad-5db0-b917-83445ba707f0",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChoiceBand.Name",
    display_name="Choice Band",
    searchable_by=["Choice Band", "Item", "Pokémon Tool", "ChoiceBand"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=162,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    passive=typed_damage_boost_tool(_gx_or_ex, BOOST, to_active_only=True),
)
