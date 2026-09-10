"""Oddish (SM - Unbroken Bonds 5/214).

Basic Grass Pokemon. HP 50, weakness Fire x2, no resistance, retreat 1.

  Stun Spore [C]      Flip a coin. If heads, your opponent's Active
                      Pokemon is now Paralyzed.
  Seed Bomb  [GC] 20

Gloom in the same set evolves from this one.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (PokemonTypes, PokemonStage, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="977dcd68-2dbd-5262-ad33-579851e97429",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    display_name="Oddish",
    searchable_by=["Oddish", "Basic", "Oddish"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=43,
    abilities=[
        Attack(
            title="Stun Spore",
            game_text=("Flip a coin. If heads, your opponent's Active "
                       "Pokémon is now Paralyzed."),
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
