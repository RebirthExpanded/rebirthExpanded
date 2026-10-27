"""Simisear (SV08 23 -- JP SV7a 008; English SSP/23). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c3aed8fb-9a5b-57dd-a38d-0d9ed8dc4be4",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name",
    display_name="Simisear",
    searchable_by=["Simisear", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    family_id=513,
    abilities=[
        Attack(
            title="Double Smash",
            game_text="Flip 2 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.FIRE: 1},
            damage=70,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=70),
        ),
    ],
)
