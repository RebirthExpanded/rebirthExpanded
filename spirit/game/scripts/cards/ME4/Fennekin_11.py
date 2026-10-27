"""Fennekin (ME4 11 -- JP M4 011; English CRI/11, MEP/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="d1529fc0-8a7c-5ea9-bef0-962383a5c22b",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name",
    display_name="Fennekin",
    searchable_by=["Fennekin", "Basic"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=653,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=2, prompt="Choose up to 2 Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Steady Firebreathing",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
    ],
)
