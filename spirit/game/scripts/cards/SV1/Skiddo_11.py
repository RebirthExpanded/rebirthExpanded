"""Skiddo (SV1 11 -- JP SV1S 003; English SVI/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="f9089acf-bb9e-599c-969a-9d93ae497dc8",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name",
    display_name="Skiddo",
    searchable_by=["Skiddo", "Basic"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=672,
    abilities=[
        Attack(
            title="Vine Whip",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Smash Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
