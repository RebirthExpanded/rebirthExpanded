"""Mimikyu (ME2 42 -- JP MBD 006; English PFL/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="d38994d4-8498-5a41-8538-d9856f2b4230",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=778,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=1, prompt="Choose a Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
