"""Gothitelle (BWPJ 324 -- JP WAK 024; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="3d36eea6-4628-5c69-b55d-2c0c169d16c1",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=324,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    family_id=574,
    abilities=[
        Attack(
            title="Palm Strike",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Double Trick",
            game_text="Flip 2 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=70),
        ),
    ],
)
