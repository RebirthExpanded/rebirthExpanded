"""Bounsweet (SV4 8 -- JP SV4K 006; English PAR/8). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="863101e6-39ef-5a39-9caf-dd8a80a0845f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name",
    display_name="Bounsweet",
    searchable_by=["Bounsweet", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=761,
    abilities=[
        Attack(
            title="Quick Blow",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
