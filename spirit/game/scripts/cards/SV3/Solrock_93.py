"""Solrock (SV3 93 -- JP SV3 048; English OBF/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="ef2432cf-bcdc-504c-aa00-cc3c5a322bbe",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock", "Basic"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=338,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=2, prompt="Choose up to 2 Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Solar Beam",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
