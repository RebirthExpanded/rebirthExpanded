"""Antique Cover Fossil (SV - Black Bolt 80 -- JP SV11B 080, the art here).

Item (fossil).

  "Play this card as if it were a 60-HP Basic [C] Pokemon. This card
   can't be affected by any Special Conditions and can't retreat. At any
   time during your turn, you may discard this card from play."

  Ability  Cover Protection  Prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon.

Antique Armor Fossil's shape: FossilItemCardDef with FossilBodyPassive
(no Special Conditions, no retreat) plus the discard Ability.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability
from spirit.game.data_utils import Ability, FossilItemCardDef
from spirit.game.card_effects.passives_common import attack_effect_shield_passive

ABILITY_PASSIVE = attack_effect_shield_passive()

card = FossilItemCardDef(
    guid="403425d3-2fb3-548f-be12-1e72c2f8716c",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueCoverFossil.Name",
    display_name="Antique Cover Fossil",
    searchable_by=["Antique Cover Fossil", "Item", "AntiqueCoverFossil"],
    subtypes=["Item"],
    collector_number=80,
    set_code="ZSV10PT5",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[
        fossil_discard_ability(),
        Ability(
            title="Cover Protection",
            game_text="Prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon.",
            passive=ABILITY_PASSIVE,
        ),
    ],
)
