"""Bruxish (SV1 51 -- JP SV1S 017; English SVI/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="841f15f5-72d1-5741-89c3-acf00339d7ce",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bruxish.Name",
    display_name="Bruxish",
    searchable_by=["Bruxish", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=779,
    abilities=[
        Attack(
            title="Vivid Charge",
            game_text="Search your deck for up to 3 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=su.search_to_hand(is_basic_energy_card, count=3, reveal=True, prompt="Choose up to 3 Basic Energy cards."),
        ),
        Attack(
            title="Wave Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
