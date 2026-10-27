"""Togedemaru (ME2 73 -- JP M2 061; English PFL/104, PFL/73). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


card = PokemonCardDef(
    guid="48bae4d3-07cc-5518-bcf2-856a2b5745f3",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaru.Name",
    display_name="Togedemaru",
    searchable_by=["Togedemaru", "Basic"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=777,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_pokemon_card, count=1, reveal=True, prompt="Choose a Pokémon."),
        ),
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=30,
        ),
    ],
)
