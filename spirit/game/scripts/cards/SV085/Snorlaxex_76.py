"""Snorlax ex (SV085 76 -- JP SVM 094; English PRE/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b100bcc0-18a7-57e5-a2c7-9364489737c9",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlaxex.Name",
    display_name="Snorlax ex",
    searchable_by=["Snorlax ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=76,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=446,
    abilities=[
        Attack(
            title="Strength",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
        Attack(
            title="Toss-and-Turn Press",
            game_text="Flip 3 coins. This attack does 120 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=120),
        ),
    ],
)
