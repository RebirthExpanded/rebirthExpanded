"""Pikachu (XY 42/146 -- JP "THE BEST OF XY" 029/171).

Basic Lightning. HP 60, weakness Fighting x2, resistance Metal -20,
retreat 1.

  Nuzzle        [C]      Flip a coin. If heads, your opponent's Active
                         Pokemon is now Paralyzed.
  Quick Attack  [CC] 20+ Flip a coin. If heads, this attack does 10 more
                         damage.

Both halves are the shared factories: condition_attack with flip=True for
the Paralysis, flip_bonus for the +10. Nuzzle deals no damage at all, so
its Attack carries no damage and the coin decides the whole attack.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import (condition_attack,
                                                     flip_bonus)
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="2682bbbe-22d0-5623-ad11-4cb67c80b287",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Nuzzle",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=flip_bonus(10),
        ),
    ],
)
