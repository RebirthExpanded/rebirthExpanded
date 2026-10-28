"""Pumpkaboo (SV4 77 -- JP SV4M 029; English PAR/77). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="91ea215c-a0f5-59af-8c1f-8bd5f332e14d",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    display_name="Pumpkaboo",
    searchable_by=["Pumpkaboo", "Basic"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=710,
    abilities=[
        Attack(
            title="Seed Bomb",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=ac.recoil_attack(20),
        ),
    ],
)
