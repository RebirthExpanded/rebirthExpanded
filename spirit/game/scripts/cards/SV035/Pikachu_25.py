"""Pikachu (SV035 25 -- JP SV2a 025; English MEW/173, MEW/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


card = PokemonCardDef(
    guid="bc576018-50dc-5841-bfd3-99633c423f3f",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Charge",
            game_text="Search your deck for a Basic Lightning Energy card and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=su.search_attach_energy(_basic_lightning, count=1, to_self=True, prompt="Choose a Basic Lightning Energy card to attach to this Pokémon."),
        ),
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
