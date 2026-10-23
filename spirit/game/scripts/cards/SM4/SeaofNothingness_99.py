"""Sea of Nothingness (SM - Crimson Invasion 99/111 -- JP SM4A 048/050, the art here).

Stadium.

  "Special Conditions are not removed when Pokemon (both yours and your
   opponent's) evolve or devolve."

The keeps_conditions_through_evolution hook: the evolve and devolve paths
put every Special Condition back on the new top card after the usual wipe,
with its bookkeeping (Poison counters, Sleep coins, when Paralysis began).
Official Q&A:

- A New Moon Lunatone shields its side: those Pokemon still recover.
- The new card's own immunity still cures (Dachsbun's Ability recovers a
  Burn, Grumpig's Own Tempo a Confusion).
- A BREAK Evolution keeps them too.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef
from spirit.game.session.passives import Passive


class SeaOfNothingnessPassive(Passive):
    def keeps_conditions_through_evolution(self, pokemon, carrier):
        return True


card = StadiumCardDef(
    guid="fd27b6d1-7188-5a66-b674-6d00102a0d40",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SeaofNothingness.Name",
    display_name="Sea of Nothingness",
    searchable_by=["Sea of Nothingness", "Stadium", "SeaofNothingness"],
    subtypes=["Stadium"],
    collector_number=99,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    passive=SeaOfNothingnessPassive(),
)
