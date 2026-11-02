"""Pretend Rocket Boss Pikachu (SMPJ 191 -- JP SMP 191; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="e792fd3f-144c-5f2a-ae06-e4cfa6bf8508",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PretendRocketBossPikachu.Name",
    display_name="Pretend Rocket Boss Pikachu",
    searchable_by=["Pretend Rocket Boss Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=191,
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
            title="Take Over?",
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=su.gust_attack(),
        ),
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
