"""Voltorb (XY - Roaring Skies 21/108 -- JP XY6-B 016/078).

Basic Lightning Pokemon. HP 60, weakness Fighting x2, resistance Metal
-20, retreat 1.

  Thunder Wave   [L]     Flip a coin. If heads, your opponent's Active
                         Pokemon is now Paralyzed.
  Big Explosion  [LC] 60  This Pokemon does 60 damage to itself.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import (condition_attack,
                                                     recoil_attack)
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="a9202bbb-18bd-5186-a307-1dc9cc62c837",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    display_name="Voltorb",
    searchable_by=["Voltorb", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="XY6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=100,
    abilities=[
        Attack(
            title="Thunder Wave",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Big Explosion",
            game_text="This Pokémon does 60 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=recoil_attack(60),
        ),
    ],
)
