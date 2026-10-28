"""Numel (SV045 11 -- JP SV4K 011; English PAF/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="cde9a5d2-4201-5905-af32-11bea56272e6",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    display_name="Numel",
    searchable_by=["Numel", "Basic"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=322,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Heat Blast",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
