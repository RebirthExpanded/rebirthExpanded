"""Fidough (SV07 66 -- JP SV7 045; English SCR/66). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="23c9509f-dc49-5bf6-864c-a22999b0f6b0",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fidough.Name",
    display_name="Fidough",
    searchable_by=["Fidough", "Basic"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=926,
    abilities=[
        Attack(
            title="Pleasant Aroma",
            game_text="Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=1, prompt="Choose a Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
