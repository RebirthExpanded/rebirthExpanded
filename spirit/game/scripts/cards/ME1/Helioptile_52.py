"""Helioptile (ME1 52 -- JP M1S 034; English MEG/143, MEG/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2cdc6570-d5b8-594e-a5cb-21fc34c80b57",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    display_name="Helioptile",
    searchable_by=["Helioptile", "Basic"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=694,
    abilities=[
        Attack(
            title="Double Scratch",
            game_text="Flip 2 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=10),
        ),
    ],
)
