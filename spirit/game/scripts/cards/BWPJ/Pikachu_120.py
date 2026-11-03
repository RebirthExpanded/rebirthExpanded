"""Pikachu (BWPJ 120 -- JP BWP 120; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="d938adaa-4ffc-5505-b9da-8e2b6a8fa796",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=pc.flip_protection(effects_too=True),
        ),
        Attack(
            title="Gather Strength",
            game_text="Search your deck for 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=su.search_to_hand(is_basic_energy_card, count=2, reveal=True, prompt="Choose up to 2 Basic Energy cards."),
        ),
    ],
)
