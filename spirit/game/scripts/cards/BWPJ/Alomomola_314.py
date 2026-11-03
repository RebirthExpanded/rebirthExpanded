"""Alomomola (BWPJ 314 -- JP WAK 014; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7b7ec8ef-9faf-5507-b7c8-523c6ab6026e",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name",
    display_name="Alomomola",
    searchable_by=["Alomomola", "Basic"],
    subtypes=["Basic"],
    collector_number=314,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=594,
    abilities=[
        Attack(
            title="Double Slap",
            game_text="Flip 2 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=30),
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
