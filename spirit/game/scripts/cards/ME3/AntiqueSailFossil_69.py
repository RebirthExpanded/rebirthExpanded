"""Antique Sail Fossil (ME - POR 69 -- JP M3 069, the art here).

Item (fossil).

  "Play this card as if it were a 60-HP Basic [C] Pokemon. This card
   can't be affected by any Special Conditions and can't retreat. At any
   time during your turn, you may discard this card from play."

  Ability  Fin Guard  Whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to this Pokémon.

Antique Armor Fossil's shape: FossilItemCardDef with FossilBodyPassive
(no Special Conditions, no retreat) plus the discard Ability.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability
from spirit.game.data_utils import Ability, FossilItemCardDef
from spirit.game.attributes import TrainerType
from spirit.game.session.passives import Passive, carrier_pokemon

class FinGuardPassive(Passive):
    """Moon & Sun Badge's shield, for this Pokemon alone."""

    def blocks_trainer_effects(self, affected_player_id, trainer_card,
                               trainer_type, carrier, affected_entity=None,
                               board=None):
        if trainer_type != TrainerType.SUPPORTER.value or affected_entity is None:
            return False
        holder = carrier_pokemon(carrier) or carrier
        return holder is (carrier_pokemon(affected_entity) or affected_entity)


ABILITY_PASSIVE = FinGuardPassive()

card = FossilItemCardDef(
    guid="789dd15b-ac97-54a6-a51b-37dc1319f5e3",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueSailFossil.Name",
    display_name="Antique Sail Fossil",
    searchable_by=["Antique Sail Fossil", "Item", "AntiqueSailFossil"],
    subtypes=["Item"],
    collector_number=69,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[
        fossil_discard_ability(),
        Ability(
            title="Fin Guard",
            game_text="Whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to this Pokémon.",
            passive=ABILITY_PASSIVE,
        ),
    ],
)
