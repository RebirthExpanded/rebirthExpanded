"""Maractus (SV045 3 -- JP SV4K 003; English PAF/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f7bc2edc-c677-50c8-a14b-cb111bcfa7ab",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name",
    display_name="Maractus",
    searchable_by=["Maractus", "Basic"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=556,
    abilities=[
        Attack(
            title="Double Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=4, per_heads=30),
        ),
    ],
)
