"""Cottonee (SV085 7 -- JP SV5K 007; English PRE/7, TEF/14). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c782399c-566c-5757-8eb2-d5069db7299f",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    display_name="Cottonee",
    searchable_by=["Cottonee", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=546,
    abilities=[
        Attack(
            title="Triple Spin",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=10),
        ),
    ],
)
