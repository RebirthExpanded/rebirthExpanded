"""Bent Spoon (XY - Fates Collide 93/124 -- JP XY10 073/078, the art here).

Pokemon Tool.

  "Prevent all effects of your opponent's attacks, except damage, done to
   the Pokemon this card is attached to. (Existing effects are not
   removed.)"

Antique Cover Fossil's Cover Protection on a Tool: the holder is shielded
from opposing attack EFFECTS (Special Conditions, damage counters placed
by an attack, "can't attack next turn", a switch-out...) while the damage
lands in full. Effects already on it stay, exactly as printed.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import attack_effect_shield_passive
from spirit.game.data_utils import PokemonToolCardDef

card = PokemonToolCardDef(
    guid="5079ad67-0935-5996-965e-fa272dab69e5",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BentSpoon.Name",
    display_name="Bent Spoon",
    searchable_by=["Bent Spoon", "Pokémon Tool", "BentSpoon"],
    subtypes=["Pokémon Tool"],
    collector_number=93,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    passive=attack_effect_shield_passive(),
)
