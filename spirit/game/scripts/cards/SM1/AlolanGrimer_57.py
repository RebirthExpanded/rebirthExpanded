"""Alolan Grimer (SM - Sun & Moon 57/149 -- JP SM1M 022/060).

Basic Psychic. HP 80, weakness Psychic x2, retreat 3.

  Super Poison Breath  [C]     Flip a coin. If heads, your opponent's
                               Active Pokemon is now Poisoned.
  Pound                [PCC] 40

Alolan Muk's own pre-evolution, printed in the same set. Nothing but the
shared coin-flip condition factory.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="55dc2a0c-cede-54e0-8f02-9dc147455aaf",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name",
    display_name="Alolan Grimer",
    searchable_by=["Alolan Grimer", "Basic", "AlolanGrimer"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=88,
    abilities=[
        Attack(
            title="Super Poison Breath",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Pound",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
