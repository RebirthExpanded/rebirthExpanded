"""Antique Jaw Fossil (ME - POR 68 -- JP M3 068, the art here).

Item (fossil).

  "Play this card as if it were a 60-HP Basic [C] Pokemon. This card
   can't be affected by any Special Conditions and can't retreat. At any
   time during your turn, you may discard this card from play."

  Ability  Intimidating Jaw  As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon do 30 less damage (before applying Weakness and Resistance).

Antique Armor Fossil's shape: FossilItemCardDef with FossilBodyPassive
(no Special Conditions, no retreat) plus the discard Ability.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability
from spirit.game.data_utils import Ability, FossilItemCardDef
from spirit.game.card_effects.passives_common import is_in_active_spot, opposing_active
from spirit.game.session.passives import Passive

class IntimidatingJawPassive(Passive):
    """Stoutland's Intimidating Fang on a fossil."""

    def modify_damage_dealt(self, calc, carrier):
        if not is_in_active_spot(carrier):
            return
        attacker = calc.attacker
        if attacker is None or not opposing_active(attacker, carrier):
            return
        calc.amount = max(0, calc.amount - 30)


ABILITY_PASSIVE = IntimidatingJawPassive()

card = FossilItemCardDef(
    guid="49741cfd-36a8-5783-b0bf-56e5e1744bf7",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueJawFossil.Name",
    display_name="Antique Jaw Fossil",
    searchable_by=["Antique Jaw Fossil", "Item", "AntiqueJawFossil"],
    subtypes=["Item"],
    collector_number=68,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[
        fossil_discard_ability(),
        Ability(
            title="Intimidating Jaw",
            game_text="As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon do 30 less damage (before applying Weakness and Resistance).",
            passive=ABILITY_PASSIVE,
        ),
    ],
)
