"""Metal Core Barrier (SM - Unbroken Bonds 180/214 -- JP SM9b 046/054, the art here).

Pokemon Tool.

  "The Pokemon this card is attached to takes 70 less damage from your
   opponent's attacks (after applying Weakness and Resistance)."
  "Discard this card at the end of your opponent's turn."

Rigid Band's reduction with Bursting Balloon's fuse
(discard_at_opponents_turn_end).
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.data_utils import PokemonToolCardDef

REDUCTION = 70

card = PokemonToolCardDef(
    guid="28cd5017-d731-5b1b-a6c3-4fbccecdcb87",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalCoreBarrier.Name",
    display_name="Metal Core Barrier",
    searchable_by=["Metal Core Barrier", "Item", "Pokémon Tool", "MetalCoreBarrier"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=180,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    discard_at_opponents_turn_end=True,
    passive=takes_less_passive(REDUCTION, protects="carrier"),
)
