"""Clefairy (SV3 81 -- JP SVD 047; English OBF/81). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b469252c-e825-590e-8d53-1a4ff9981eef",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=173,
    abilities=[
        Attack(
            title="Slap Slap",
            game_text="Flip 2 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=30),
        ),
    ],
)
