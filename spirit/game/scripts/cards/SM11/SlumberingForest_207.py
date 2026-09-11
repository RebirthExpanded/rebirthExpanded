"""Slumbering Forest (SM - Unified Minds 207/236 -- JP SM11 088/094).

Stadium.

  "If a Pokemon is Asleep, its owner flips 2 coins instead of 1 for that
   Special Condition between turns. If either of them is tails, that
   Pokemon is still Asleep."

A new passive hook, sleep_checkup_coins: the Checkup's wake-up flip asks
the board how many coins to throw and takes the largest answer, with the
attack that put the Pokemon to sleep (Thumping Snore's 2) and this Stadium
both able to raise it. Every coin has to be heads, which the Checkup
already required.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef
from spirit.game.session.passives import Passive


class SlumberingForestPassive(Passive):
    """Everyone's sleepers flip 2 to wake up."""

    def sleep_checkup_coins(self, pokemon, carrier):
        return 2


card = StadiumCardDef(
    passive=SlumberingForestPassive(),
    guid="de2407b8-1770-5b6f-9eb8-35043314f2aa",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SlumberingForest.Name",
    display_name="Slumbering Forest",
    searchable_by=["Slumbering Forest", "Stadium", "SlumberingForest"],
    subtypes=["Stadium"],
    collector_number=207,
    set_code="SM11",
    rarity=Rarities.Uncommon,
)
