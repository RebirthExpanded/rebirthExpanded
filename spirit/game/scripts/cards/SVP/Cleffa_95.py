"""Cleffa (SVP 95 -- JP SVP 092; English SVP/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="272f2c7d-6f0a-5b24-a95e-8a4cc2cdcdeb",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Basic"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=173,
    abilities=[
        Attack(
            title="Twinkling Hope",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={},
            effect=su.search_to_hand(is_basic_energy_card, count=2, reveal=True, prompt="Choose up to 2 Basic Energy cards."),
        ),
    ],
)
