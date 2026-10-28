"""Antique Dome Fossil (SV035 152 -- JP SV2a 155; English MEW/152). Japanese art.
Item (fossil).
  "Play this card as if it were a 60-HP Basic [C] Pokemon. This card
   can't be affected by any Special Conditions and can't retreat. At any
   time during your turn, you may discard this card from play."
  Ability  Domed Armor  This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).
Antique Cover Fossil's shape: FossilItemCardDef with FossilBodyPassive
plus the discard Ability.
"""
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability
from spirit.game.data_utils import Ability, FossilItemCardDef
from spirit.game.card_effects.passives_common import takes_less_passive

ABILITY_PASSIVE = takes_less_passive(30)

card = FossilItemCardDef(
    guid="e70c1a8f-055f-57c7-96d0-70da53a33146",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueDomeFossil.Name",
    display_name="Antique Dome Fossil",
    searchable_by=["Antique Dome Fossil", "Item", "AntiqueDomeFossil"],
    subtypes=["Item"],
    collector_number=152,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[
        fossil_discard_ability(),
        Ability(
            title="Domed Armor",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=ABILITY_PASSIVE,
        ),
    ],
)
