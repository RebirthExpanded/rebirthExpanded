"""Scatterbug (SV08 5 -- JP SV8 004; English SSP/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="6935ee5f-74d0-56fd-9c1f-8598ea1efca3",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name",
    display_name="Scatterbug",
    searchable_by=["Scatterbug", "Basic"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=664,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=1, prompt="Choose a Basic Pokémon to put onto your Bench."),
        ),
    ],
)
