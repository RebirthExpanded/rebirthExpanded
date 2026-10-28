"""Weedle (SV035 13 -- JP SV2a 013; English MEW/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="79033b1f-9ca7-5411-a742-7a614e2b46d0",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    display_name="Weedle",
    searchable_by=["Weedle", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=13,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Bug Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
