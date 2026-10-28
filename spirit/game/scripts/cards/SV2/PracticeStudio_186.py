"""Practice Studio (SV2 186 -- JP SV1a 071; English PAL/186). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.session.effects import is_stage1_pokemon


class PracticeStudioPassive(Passive):
    """Stage 1 Pokemon's attacks do 10 more to the opponent's Active (before W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        if (calc.is_attack and calc.is_opposing and calc.to_active and calc.attacker is not None
                and is_stage1_pokemon(calc.attacker)):
            calc.amount += 10


card = StadiumCardDef(
    guid="058d358b-0100-577b-90df-382cdbaa0a3c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PracticeStudio.Name",
    display_name="Practice Studio",
    searchable_by=["Practice Studio", "Stadium"],
    subtypes=["Stadium"],
    collector_number=186,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    passive=PracticeStudioPassive(),
)
