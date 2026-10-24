"""XY Ancient Traits (Primal Clash .. Ancient Origins).

Ancient Traits are not Abilities: Ability locks (Garbotoxin, Silent Lab, Path
to the Peak) never switch them off. Each trait is an Ability entry with
ability_type=ANCIENT_TRAIT so the client draws the trait banner, and its
passive rides it like an Ability passive (passives.py exempts it from locks).

Traits that live in the engine rather than in a passive are looked up by
title with has_ancient_trait: alpha Growth (the second Energy on a manual
attachment, GameSession._execute_attach_energy) and alpha Recovery (doubled
heals, EffectContext.heal).
"""

from typing import Optional

from spirit.game.attributes import AbilityTypes, AttrID
from spirit.game.card_effects.passives_common import (
    OmegaBarrierPassive, ability_effect_shield_passive,
)
from spirit.game.card_effects.pokemon import AttackTwicePassive
from spirit.game.data_utils import ABILITIES_BY_ID, Ability
from spirit.game.session.passives import Passive, carrier_pokemon

OMEGA_BARRIER = "Ω Barrier"
OMEGA_BARRAGE = "Ω Barrage"
ALPHA_GROWTH = "α Growth"
ALPHA_RECOVERY = "α Recovery"
THETA_STOP = "θ Stop"
THETA_DOUBLE = "θ Double"


def has_ancient_trait(pokemon, title: str) -> bool:
    """Whether an in-play Pokemon's top card carries the named trait."""
    if pokemon is None:
        return False
    for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
        if not isinstance(entry, dict):
            continue
        ability = ABILITIES_BY_ID.get(entry.get("abilityID"))
        if ability is not None and ability.ability_type == AbilityTypes.ANCIENT_TRAIT \
                and ability.title == title:
            return True
    return False


class ThetaDoublePassive(Passive):
    """This Pokemon may have up to 2 Pokemon Tool cards attached to it."""

    def tool_capacity(self, pokemon, carrier):
        return 2 if pokemon is carrier_pokemon(carrier) else 1


TRAIT_TEXT = {
    OMEGA_BARRIER: "Whenever your opponent plays a Trainer card (excluding Pokémon Tools and Stadium cards), prevent all effects of that card done to this Pokémon.",
    OMEGA_BARRAGE: "This Pokémon may attack twice a turn. (If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.)",
    ALPHA_GROWTH: "When you attach an Energy card from your hand to this Pokémon (except with an attack, Ability, or Trainer card), you may attach 2 Energy cards.",
    ALPHA_RECOVERY: "When this Pokémon is healed, double the amount healed.",
    THETA_STOP: "Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon.",
    THETA_DOUBLE: "This Pokémon may have up to 2 Pokémon Tool cards attached to it.",
}


def ancient_trait(title: str, game_text: Optional[str] = None) -> Ability:
    """A fresh Ability entry for an Ancient Trait (one instance per print)."""
    passive = {
        OMEGA_BARRIER: OmegaBarrierPassive,
        OMEGA_BARRAGE: AttackTwicePassive,
        THETA_STOP: ability_effect_shield_passive,
        THETA_DOUBLE: ThetaDoublePassive,
    }.get(title)
    return Ability(title=title, game_text=game_text or TRAIT_TEXT.get(title, ""),
                   ability_type=AbilityTypes.ANCIENT_TRAIT,
                   passive=passive() if passive is not None else None)
