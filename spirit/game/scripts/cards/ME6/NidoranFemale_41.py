"""Nidoran ♀ (ME6 41 -- JP M6 041; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


card = PokemonCardDef(
    guid="e65755c7-ce71-59b7-8a06-a9922f23b671",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NidoranFemale.Name",
    display_name="Nidoran ♀",
    searchable_by=["Nidoran ♀", "Basic"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=29,
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
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
