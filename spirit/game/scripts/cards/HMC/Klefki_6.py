"""Klefki (JP XY Hyper Metal Chain Deck 60 -- HMC 006/018; English print
XY - Phantom Forces 66/119).

Basic Metal Pokemon. HP 70, weakness Fire x2, resistance Psychic -20,
retreat 1.

  Call for Family  [M]     Search your deck for up to 2 Basic Pokemon and
                           put them onto your Bench. Shuffle your deck
                           afterward.
  Dull Light       [MC] 20  Your opponent's Active Pokemon is now Confused.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="a88e550f-d715-5f22-ae08-fc9a798261a4",
    key="HMC",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="HMC",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=707,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.METAL: 1},
            damage=0,
            effect=search_to_bench(count=2),
        ),
        Attack(
            title="Dull Light",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
