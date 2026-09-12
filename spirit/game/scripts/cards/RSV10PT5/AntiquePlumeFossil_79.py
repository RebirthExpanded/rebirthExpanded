"""Antique Plume Fossil (SV - White Flare 79 -- JP MC 657 (Start Deck 100), the art here).

Item (fossil).

  "Play this card as if it were a 60-HP Basic [C] Pokemon. This card
   can't be affected by any Special Conditions and can't retreat. At any
   time during your turn, you may discard this card from play."

  Ability  Wing Guard  As long as this Pokémon is on the Bench, prevent all damage done to it by attacks from your opponent's Pokémon.

Antique Armor Fossil's shape: FossilItemCardDef with FossilBodyPassive
(no Special Conditions, no retreat) plus the discard Ability.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability
from spirit.game.data_utils import Ability, FossilItemCardDef
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive

class WingGuardPassive(Passive):
    def prevents_damage(self, calc, carrier):
        return (calc.is_attack and calc.is_opposing and calc.target is carrier
                and not is_in_active_spot(carrier))


ABILITY_PASSIVE = WingGuardPassive()

card = FossilItemCardDef(
    guid="817012d0-6f81-567a-8540-bbf83dcd1922",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiquePlumeFossil.Name",
    display_name="Antique Plume Fossil",
    searchable_by=["Antique Plume Fossil", "Item", "AntiquePlumeFossil"],
    subtypes=["Item"],
    collector_number=79,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[
        fossil_discard_ability(),
        Ability(
            title="Wing Guard",
            game_text="As long as this Pokémon is on the Bench, prevent all damage done to it by attacks from your opponent's Pokémon.",
            passive=ABILITY_PASSIVE,
        ),
    ],
)
