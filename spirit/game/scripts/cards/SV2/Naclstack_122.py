"""Naclstack (SV2 122 -- JP SV2D 047; English PAF/177, PAL/122). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9192f7c1-2814-52e9-9e0d-be4b0e2ba8c7",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    display_name="Naclstack",
    searchable_by=["Naclstack", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=122,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name",
    family_id=932,
    abilities=[
        Attack(
            title="Salt Cannon",
            game_text="Flip 3 coins. This attack does 60 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=60),
        ),
    ],
)
