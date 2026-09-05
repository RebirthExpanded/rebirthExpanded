"""Float Stone (XY - BREAKthrough 137/162).

Pokemon Tool.

  "The Pokemon this card is attached to has no Retreat Cost."

Air Balloon with the subtraction replaced by a floor: same
modify_retreat_cost hook, same carrier_pokemon(carrier) is pokemon test for
"the Pokemon this card is attached to", and the passive lives beside
Air Balloon's in card_effects/trainers.py.

Charmander (ME2 11) reaches the same result through retreat_free_when, but
that factory's predicate takes (pokemon, carrier) where the carrier is the
Pokemon itself. A Tool's carrier is the Tool, so this reads the holder off
the attachment stack instead.

The two other sentences on the card are the standard Tool and Item rules
the engine already enforces, not card-specific behavior.
"""

from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FloatStonePassive

card = PokemonToolCardDef(
    guid="5d073628-31df-5dd0-91f1-df851a226be7",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FloatStone.Name",
    display_name="Float Stone",
    searchable_by=["Float Stone", "Pok\u00e9mon Tool", "FloatStone"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=137,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=FloatStonePassive(),
)
