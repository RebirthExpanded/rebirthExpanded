"""Kirlia (ME1 59 -- JP M1S 041; English ASC/88, MEG/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


card = PokemonCardDef(
    guid="90685770-3d7d-507f-9921-ffaec0fd6c2a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    display_name="Kirlia",
    searchable_by=["Kirlia", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Call Sign",
            game_text="Search your deck for up to 3 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=su.search_to_hand(is_pokemon_card, count=3, reveal=True, prompt="Choose up to 3 Pokémon."),
        ),
        Attack(
            title="Psyshot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
    ],
)
