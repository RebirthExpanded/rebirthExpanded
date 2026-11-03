"""Pangoro (XYPJ 402 -- JP XYC 002; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2c6e99a6-9b59-5885-ac8c-ab192bcb7d3c",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pangoro.Name",
    display_name="Pangoro",
    searchable_by=["Pangoro", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=402,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    family_id=674,
    abilities=[
        Attack(
            title="Damage Rush",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.flip_damage(until_tails=True, bonus_per_heads=30),
        ),
        Attack(
            title="Double Lariat",
            game_text="Flip 2 coins. This attack does 80 damage for each heads.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=80),
        ),
    ],
)
