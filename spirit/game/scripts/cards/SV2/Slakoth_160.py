"""Slakoth (SV - Paldea Evolved 160/193).

Basic Colorless Pokemon. HP 70, weakness Fighting x2, no resistance,
retreat 2.

  Yawn [CC]  Your opponent's Active Pokemon is now Asleep.

No damage at all -- the sleep is the whole attack. Vigoroth and Slaking ex
sit above it in the family.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (PokemonTypes, PokemonStage, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="0aea75f1-ab5f-53b8-8be3-3159ca48ed68",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    display_name="Slakoth",
    searchable_by=["Slakoth", "Basic", "Slakoth"],
    subtypes=["Basic"],
    collector_number=160,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=287,
    abilities=[
        Attack(
            title="Yawn",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
