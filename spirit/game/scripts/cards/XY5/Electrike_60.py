"""Electrike (XY - Primal Clash 60/160 -- JP XY5-Bg 022/070).

Basic Lightning Pokemon. HP 50, weakness Fighting x2, resistance Metal
-20, retreat 1.

  Ancient Trait  Ω Barrier  Whenever your opponent plays a Trainer card
                            (excluding Pokemon Tools and Stadium cards),
                            prevent all effects of that card done to this
                            Pokemon.
  Thunder Fang  [L] 10  Flip a coin. If heads, your opponent's Active
                        Pokemon is now Paralyzed.

The pool's second Ancient Trait and its first Ω Barrier: an entity-scoped
shield against the opponent's Items and Supporters, sharing
OmegaBarrierPassive with Regirock. The rulings it follows: a Guzma
pointed at an Ω Barrier bencher is playable and does nothing; an Escape
Rope is done to the Active, so it stays playable with only Ω Barrier
Pokemon on the Bench, and with an Ω Barrier ACTIVE only the Escape Rope
player switches. Being an Ancient Trait and not an Ability, no ability
lock reaches it.
"""

from spirit.game.attributes import (AbilityTypes, PokemonStage, PokemonTypes,
                                    Rarities, SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import OmegaBarrierPassive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef

card = PokemonCardDef(
    guid="34227363-b033-5ad0-ac9d-176100f5a13d",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    display_name="Electrike",
    searchable_by=["Electrike", "Basic"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=309,
    abilities=[
        Ability(
            title="Ω Barrier",
            game_text="Whenever your opponent plays a Trainer card (excluding Pokémon Tools and Stadium cards), prevent all effects of that card done to this Pokémon.",
            ability_type=AbilityTypes.ANCIENT_TRAIT,
            passive=OmegaBarrierPassive(),
        ),
        Attack(
            title="Thunder Fang",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
