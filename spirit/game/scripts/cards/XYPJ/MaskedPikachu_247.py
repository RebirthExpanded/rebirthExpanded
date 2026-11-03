"""Masked Pikachu (XYPJ 247 -- JP XYP 247; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="662de32d-5cb3-5990-96ae-e13b15312da3",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MaskedPikachu.Name",
    display_name="Masked Pikachu",
    searchable_by=["Masked Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=247,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
        Attack(
            title="Flying Elekick",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
