"""Panpour (SV4 41 -- JP SV4M 015; English PAR/41). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5936513f-9bdd-56f8-8d19-a95c0ff6d40a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name",
    display_name="Panpour",
    searchable_by=["Panpour", "Basic"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=515,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=1, prompt="Choose a Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
