"""Martial Arts Dojo (SM - Unbroken Bonds 179/214 -- JP SM10 089/095, the art here).

Stadium.

  "The attacks of non-Ultra Beast Pokemon that have any basic Energy
   attached to them (both yours and your opponent's) do 10 more damage to
   the opponent's Active Pokemon (before applying Weakness and
   Resistance). If the attacking player has more Prize cards remaining
   than their opponent, those attacks do 40 more damage instead."

Both sides, read live: the +40 half asks about the ATTACKER's Prize
count at the moment the damage is figured, so it turns on and off as the
race swings.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import more_prizes_remaining_than_opponent
from spirit.game.card_effects.trainers import is_basic_energy_card, is_ultra_beast
from spirit.game.data_utils import StadiumCardDef
from spirit.game.session.passives import Passive

BOOST = 10
BOOST_BEHIND = 40


class MartialArtsDojoPassive(Passive):
    """+10 (or +40 while the attacker's owner leads on Prizes remaining) to
    the opposing Active, for any non-Ultra Beast carrying basic Energy."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or is_ultra_beast(attacker):
            return
        if not any(is_basic_energy_card(c) for c in attacker.children):
            return
        owner = attacker.owning_player_id
        ahead = owner is not None and more_prizes_remaining_than_opponent(calc.board, owner)
        calc.amount += BOOST_BEHIND if ahead else BOOST


card = StadiumCardDef(
    guid="801ac0f8-12dc-5465-bef9-ee7e90ccc772",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MartialArtsDojo.Name",
    display_name="Martial Arts Dojo",
    searchable_by=["Martial Arts Dojo", "Stadium", "MartialArtsDojo"],
    subtypes=["Stadium"],
    collector_number=179,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=MartialArtsDojoPassive(),
)
