"""Pikachu (SMPJ 227 -- JP SMP 227; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su


_scramble = ac.flip_or_nothing(then=su.search_to_hand(None, count=1, reveal=False, prompt="Choose a card."))


card = PokemonCardDef(
    guid="2f74a2a2-6510-5aca-b140-d130fb5a4f5b",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=227,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Spark",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title="Scramble",
            game_text="Flip a coin. If heads, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_scramble,
        ),
    ],
)
