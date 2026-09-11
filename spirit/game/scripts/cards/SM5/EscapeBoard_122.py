"""Escape Board (SM - Ultra Prism 122/156 -- JP SM5M 052/066).

Pokemon Tool.

  "The Retreat Cost of the Pokemon this card is attached to is [C] less, and
   it can retreat even if it's Asleep or Paralyzed."

Air Balloon's -2 at -1, plus a permission the pool did not have: retreating
while Asleep or Paralyzed. Attacking has carried that exemption since Windup
Arm, so retreat now has the matching one -- asked of the Active only, and
lifting the condition gate rather than the cost.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import EscapeBoardPassive
from spirit.game.data_utils import PokemonToolCardDef

card = PokemonToolCardDef(
    guid="74cc878e-f6ea-5e8f-8c47-0433d8bf3309",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeBoard.Name",
    display_name="Escape Board",
    searchable_by=["Escape Board", "Pokémon Tool", "EscapeBoard"],
    subtypes=["Pokémon Tool"],
    collector_number=122,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    passive=EscapeBoardPassive(),
)
