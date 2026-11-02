"""Pikachu (Promo_SWSH 39 -- JP SP 024; English SP/39). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.sm9 import tail_whip


card = PokemonCardDef(
    guid="104c0010-e9e9-5f86-98b9-432fcae034f5",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Tail Whip",
            game_text="Flip a coin. If heads, during your opponent's next turn, the Defending Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=tail_whip,
        ),
        Attack(
            title="Pika Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
