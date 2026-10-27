"""Gossifleur (SV07 10 -- JP SV7 008; English SCR/10). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="53d79032-2a3f-5a6e-816c-c9e9f243fba1",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gossifleur.Name",
    display_name="Gossifleur",
    searchable_by=["Gossifleur", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=829,
    abilities=[
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=10),
        ),
    ],
)
