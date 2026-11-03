"""Scrafty (BWPJ 333 -- JP WAK 033; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="081c15f6-8385-5e29-a0ca-1e5b78b3a5a0",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=333,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 60 damage for each heads.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=60),
        ),
    ],
)
