"""Serperior (BWPJ 198 -- JP BWP 198; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="3c4be491-69a7-5b23-8355-e1679b06115e",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name",
    display_name="Serperior",
    searchable_by=["Serperior", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=198,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    family_id=495,
    abilities=[
        Attack(
            title="Cut",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Cross Whip",
            game_text="Flip 4 coins. This attack does 50 damage for each heads.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=ac.flip_damage(coins=4, per_heads=50),
        ),
    ],
)
