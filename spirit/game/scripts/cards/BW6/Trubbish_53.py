"""Trubbish (BW - Dragons Exalted 53/124 -- JP BW5 027/050, the art here).

Basic Psychic Pokemon. HP 70, weakness Psychic x2, retreat 2.

  Pound       [C] 20
  Poison Gas  [PC] 30  The Defending Pokemon is now Poisoned.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="6581c00e-01ec-5c79-a276-e4fc7393759b",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    display_name="Trubbish",
    searchable_by=["Trubbish", "Basic"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="BW6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=568,
    abilities=[
        Attack(
            title="Pound",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Poison Gas",
            game_text="The Defending Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
