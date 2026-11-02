"""Yokohama's Pikachu (SMPJ 282 -- JP SMP 282; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5ae111ec-da62-55ee-877d-ee40da425da9",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YokohamasPikachu.Name",
    display_name="Yokohama's Pikachu",
    searchable_by=["Yokohama's Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=282,
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
            title="Renewal Opening!",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Triple Smash",
            game_text="Flip 3 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=20),
        ),
    ],
)
