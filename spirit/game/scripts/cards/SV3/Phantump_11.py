"""Phantump (SV3 11 -- JP SV3 007; English OBF/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="ae1e261c-925a-5756-94d3-de9c371563f0",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    display_name="Phantump",
    searchable_by=["Phantump", "Basic"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=708,
    abilities=[
        Attack(
            title="Branch Poke",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
