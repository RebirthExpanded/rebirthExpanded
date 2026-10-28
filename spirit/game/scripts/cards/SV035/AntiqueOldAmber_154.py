"""Antique Old Amber (SV035 154 -- JP SV2a 156; English MEW/154). Japanese art.
Item (fossil).
  "Play this card as if it were a 60-HP Basic [C] Pokemon. This card
   can't be affected by any Special Conditions and can't retreat. At any
   time during your turn, you may discard this card from play."
  Ability  Amber Protection  Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon.
Antique Cover Fossil's shape: FossilItemCardDef with FossilBodyPassive
plus the discard Ability.
"""
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability
from spirit.game.data_utils import Ability, FossilItemCardDef
from spirit.game.card_effects.passives_common import ability_effect_shield_passive

ABILITY_PASSIVE = ability_effect_shield_passive()

card = FossilItemCardDef(
    guid="81987ad5-a1a2-54fe-8e45-cfa27b13a3c6",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueOldAmber.Name",
    display_name="Antique Old Amber",
    searchable_by=["Antique Old Amber", "Item", "AntiqueOldAmber"],
    subtypes=["Item"],
    collector_number=154,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[
        fossil_discard_ability(),
        Ability(
            title="Amber Protection",
            game_text="Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon.",
            passive=ABILITY_PASSIVE,
        ),
    ],
)
