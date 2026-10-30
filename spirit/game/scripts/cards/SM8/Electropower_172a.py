"""Electropower (SM - Lost Thunder 172/214 -- JP SM7a 054/060).

Item.

  "During this turn, your Lightning Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."

Power Tablet with the gate on the attacker's TYPE instead of a subtype:
a TurnDamageModifier with a source predicate, and the same green up-arrow
on every Lightning Pokemon of yours in play.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import electropower
from spirit.game.data_utils import ItemCardDef

card = ItemCardDef(
    guid="5ac0501b-4682-5255-b24f-744b6dcddaa2",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electropower.Name",
    display_name="Electropower",
    searchable_by=["Electropower", "Item", "Electropower"],
    subtypes=["Item"],
    collector_number=237,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=electropower,
    condition=None,
)
