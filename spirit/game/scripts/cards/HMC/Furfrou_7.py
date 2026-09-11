"""Furfrou (JP XY Hyper Metal Chain Deck 60 -- HMC 007/018; English print
XY - Phantom Forces 90/119).

Basic Colorless Pokemon. HP 90, weakness Fighting x2, retreat 1.

  Tight Jaw   [CC] 20   Flip a coin. If heads, your opponent's Active
                        Pokemon is now Paralyzed.
  Sharp Fang  [CCC] 50
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="3f42da97-5849-5f64-a81f-8a90a0bbb5ae",
    key="HMC",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name",
    display_name="Furfrou",
    searchable_by=["Furfrou", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="HMC",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=676,
    abilities=[
        Attack(
            title="Tight Jaw",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(title="Sharp Fang", game_text="",
               cost={PokemonTypes.COLORLESS: 3}, damage=50),
    ],
)
