"""Tandemaus (SV1 160 -- JP SV1V 065; English SVI/160). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="53cc6d59-8cd8-541b-85b0-db0a5cd5ef81",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    display_name="Tandemaus",
    searchable_by=["Tandemaus", "Basic"],
    subtypes=["Basic"],
    collector_number=160,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=924,
    abilities=[
        Attack(
            title="Double Hit",
            game_text="Flip 2 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=30),
        ),
    ],
)
