"""Dedenne (SV045 36 -- JP SVEM 009; English PAF/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="aab967ab-bfc8-5a56-86fd-f28182150753",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=702,
    abilities=[
        Attack(
            title="Minor Errand-Running",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=su.search_to_hand(is_basic_energy_card, count=2, reveal=True, prompt="Choose up to 2 Basic Energy cards."),
        ),
        Attack(
            title="Spin Turn",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=su.switch_self_attack(),
        ),
    ],
)
