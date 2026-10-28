"""Pineco (SV045 1 -- JP SV2D 004; English PAF/1, PAF/99, PAL/4, SVP/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="142fae55-7be3-598e-aa90-5cf43513170e",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    display_name="Pineco",
    searchable_by=["Pineco", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=204,
    abilities=[
        Attack(
            title="Rollout",
            game_text="",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)
