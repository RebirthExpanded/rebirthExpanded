"""Zorua (BW - Dark Explorers 70/108 -- JP BW-P 116 promo).

Basic Darkness. HP 60, weakness Fighting x2, resistance Psychic -20,
retreat 1.

  Paralyzing Gaze  [C]     Flip a coin. If heads, your opponent's Active
                           Pokemon is now Paralyzed.
  Shadow Bind      [DC] 20 During your opponent's next turn, the Defending
                           Pokemon can't retreat.

Zoroark-GX's partner, and both halves are shared factories: the coin-gated
condition and the retreat lock. The Japanese card is the Dark Rush promo
printing of the Dark Explorers card, which is what the promo's own art
stamp says.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="e2c10341-fb15-5cca-9256-14e2096a0322",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    display_name="Zorua",
    searchable_by=["Zorua", "Basic", "Zorua"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=570,
    abilities=[
        Attack(
            title="Paralyzing Gaze",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Shadow Bind",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)
