"""Defiance Band (SV - Scarlet & Violet 169/198 -- JP SV1S 073/078).

Pokemon Tool.  "If you have more Prize cards remaining than your opponent,
the attacks of the Pokemon this card is attached to do 30 more damage to
your opponent's Active Pokemon (before applying Weakness and Resistance)."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import more_prizes_remaining_than_opponent
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class DefianceBandPassive(Passive):
    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        holder = carrier_pokemon(carrier)
        if holder is not calc.attacker:
            return
        if more_prizes_remaining_than_opponent(calc.board, holder.owning_player_id):
            calc.amount += 30


card = PokemonToolCardDef(
    guid="b5314d6d-cc0c-5672-98ce-c8ec9ec53c2e",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DefianceBand.Name",
    display_name="Defiance Band",
    searchable_by=["Defiance Band", "Pokémon Tool", "DefianceBand"],
    subtypes=["Pokémon Tool"],
    collector_number=169,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    passive=DefianceBandPassive(),
)
