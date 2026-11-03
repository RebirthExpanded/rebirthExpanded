"""Japan National Team's Pikachu (XYPJ 50 -- JP XYP 050; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5d0cdc11-c7b8-5e38-8e84-e7ab94628a2d",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JapanNationalTeamsPikachu.Name",
    display_name="Japan National Team's Pikachu",
    searchable_by=["Japan National Team's Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Huddle",
            game_text="Heal 20 damage from each of your Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=su.heal_targets(20, "each_own"),
        ),
        Attack(
            title="Hat Trick",
            game_text="Flip 3 coins. This attack does 50 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=50),
        ),
    ],
)
