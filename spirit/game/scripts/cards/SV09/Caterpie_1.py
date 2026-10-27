"""Caterpie (SV09 1 -- JP SV9 001; English JTG/1). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="07cd1d20-d04f-50ad-ab02-9bffd2e10f05",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    display_name="Caterpie",
    searchable_by=["Caterpie", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=10,
    abilities=[
        Attack(
            title="Bug Bite",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
