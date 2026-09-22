"""Wela Volcano Park (SM - Dragon Majesty 63/70 -- JP SM6a 051/053, the art here).

Stadium.

  "Whenever a player flips a coin for the Special Condition Burned
   between turns, that Special Condition isn't removed even if the result
   is heads."

Both sides; the Burn damage still happens, only the recovery coin loses
its meaning (blocks_burn_recovery).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef
from spirit.game.session.passives import Passive


class WelaVolcanoParkPassive(Passive):
    """Burn is never cured at the Checkup, on either side."""

    def blocks_burn_recovery(self, pokemon, carrier):
        return True


card = StadiumCardDef(
    guid="07f73f9d-aaae-50f1-8a56-ddf0aef2db74",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WelaVolcanoPark.Name",
    display_name="Wela Volcano Park",
    searchable_by=["Wela Volcano Park", "Stadium", "WelaVolcanoPark"],
    subtypes=["Stadium"],
    collector_number=63,
    set_code="DM",
    rarity=Rarities.Uncommon,
    passive=WelaVolcanoParkPassive(),
)
