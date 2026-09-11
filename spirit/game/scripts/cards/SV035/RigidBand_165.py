"""Rigid Band (SV - 151 165/165 -- JP SV2a 159/165).

Pokemon Tool.  "The Stage 1 Pokemon this card is attached to takes 30 less
damage from attacks from your opponent's Pokemon (after applying Weakness
and Resistance)."
"""

from spirit.game.attributes import AttrID, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.data_utils import PokemonToolCardDef


def _stage_one_holder(target, carrier):
    from spirit.game.session.passives import carrier_pokemon
    holder = carrier_pokemon(carrier)
    return holder is target and holder.get_attribute(AttrID.STAGE) == PokemonStage.STAGE1.value


card = PokemonToolCardDef(
    guid="f07272d7-eeb0-590d-b7bb-f8b78dfe9626",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RigidBand.Name",
    display_name="Rigid Band",
    searchable_by=["Rigid Band", "Pokémon Tool", "RigidBand"],
    subtypes=["Pokémon Tool"],
    collector_number=165,
    set_code="SV035",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    passive=takes_less_passive(30, protects=_stage_one_holder),
)
