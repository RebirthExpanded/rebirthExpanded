"""Rellor (SV2 26 -- JP SV2P 014; English PAF/108, PAL/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b2180ba0-cacf-5eff-9760-95d3e7d402d1",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    display_name="Rellor",
    searchable_by=["Rellor", "Basic"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=953,
    abilities=[
        Attack(
            title="Ball Roll",
            game_text="Flip a coin until you get tails. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=30),
        ),
    ],
)
