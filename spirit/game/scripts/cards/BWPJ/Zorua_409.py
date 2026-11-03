"""Zorua (BWPJ 409 -- JP CS1 009; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="8ee55558-7d2a-514b-a359-35ded59e4df7",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    display_name="Zorua",
    searchable_by=["Zorua", "Basic"],
    subtypes=["Basic"],
    collector_number=409,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=570,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=10),
        ),
    ],
)
