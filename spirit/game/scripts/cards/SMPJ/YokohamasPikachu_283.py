"""Yokohama's Pikachu (SMPJ 283 -- JP SMP 283; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="a6ac5e26-2eaf-598b-9300-64033d29eb50",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YokohamasPikachu.Name",
    display_name="Yokohama's Pikachu",
    searchable_by=["Yokohama's Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=283,
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
            title="Wave Runner",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Electro Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
