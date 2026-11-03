"""Court Noble & Maiko Pikachu (XYPJ 221 -- JP XYP 221; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="811a1430-e1d5-5f6e-b60f-5cc74d38a7d1",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CourtNobleMaikoPikachu.Name",
    display_name="Court Noble & Maiko Pikachu",
    searchable_by=["Court Noble & Maiko Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=221,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Welcome",
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=su.gust_attack(),
        ),
        Attack(
            title="Double Bolt",
            game_text="Flip 2 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=30),
        ),
    ],
)
