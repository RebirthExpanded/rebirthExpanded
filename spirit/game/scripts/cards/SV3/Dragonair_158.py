"""Dragonair (SV3 158 -- JP SVD 089; English OBF/158). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="fe0a48f4-d694-50c0-b42d-f5b14570be36",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=["Dragonair", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=158,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Dragon Tail",
            game_text="Flip 2 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=70,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=70),
        ),
    ],
)
