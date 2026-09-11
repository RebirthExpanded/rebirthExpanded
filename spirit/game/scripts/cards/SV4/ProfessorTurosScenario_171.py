"""Professor Turo's Scenario (SV - Paradox Rift 171/182 -- JP SV4M 073/066).

Supporter.

  "Put 1 of your Pokemon in play into your hand. (Discard all cards attached
   to that Pokemon.)"

Any of your Pokemon, evolved ones included -- and only the top card comes
back, since everything attached to it (Energy, Tools and the stages
underneath) is discarded. That is the one difference from Acerola and Penny,
which hand the whole pile back.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import professor_turos_scenario
from spirit.game.data_utils import SupporterCardDef

card = SupporterCardDef(
    guid="522644e1-c6b9-5c86-98bf-44b3caee5725",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorTurosScenario.Name",
    display_name="Professor Turo's Scenario",
    searchable_by=["Professor Turo's Scenario", "Supporter",
                   "ProfessorTurosScenario"],
    subtypes=["Supporter"],
    collector_number=171,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=professor_turos_scenario,
)
