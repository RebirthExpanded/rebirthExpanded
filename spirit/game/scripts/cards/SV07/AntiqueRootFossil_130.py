"""Antique Root Fossil (SV - Stellar Crown 130 -- JP SV7 090, the art here).

Item (fossil).

  "Play this card as if it were a 60-HP Basic [C] Pokemon. This card
   can't be affected by any Special Conditions and can't retreat. At any
   time during your turn, you may discard this card from play."

  Ability  Ancient Root  As long as this Pokémon is in the Active Spot, attacks used by your opponent's Basic Pokémon cost [C] more.

Antique Armor Fossil's shape: FossilItemCardDef with FossilBodyPassive
(no Special Conditions, no retreat) plus the discard Ability.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability
from spirit.game.data_utils import Ability, FossilItemCardDef
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.effects import is_basic_pokemon_in_play
from spirit.game.session.passives import Passive

class AncientRootPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if not is_in_active_spot(carrier):
            return cost
        if pokemon.owning_player_id == carrier.owning_player_id:
            return cost
        if not is_basic_pokemon_in_play(pokemon):
            return cost
        cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


ABILITY_PASSIVE = AncientRootPassive()

card = FossilItemCardDef(
    guid="6279046b-96ae-50fd-8229-51f5cdfc047c",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueRootFossil.Name",
    display_name="Antique Root Fossil",
    searchable_by=["Antique Root Fossil", "Item", "AntiqueRootFossil"],
    subtypes=["Item"],
    collector_number=130,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[
        fossil_discard_ability(),
        Ability(
            title="Ancient Root",
            game_text="As long as this Pokémon is in the Active Spot, attacks used by your opponent's Basic Pokémon cost [C] more.",
            passive=ABILITY_PASSIVE,
        ),
    ],
)
