"""Wurmple (ME2PT5 11 -- JP M2a 004; English ASC/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="9347158d-8dbb-563d-98be-13015923f232",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    display_name="Wurmple",
    searchable_by=["Wurmple", "Basic"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=265,
    abilities=[
        Attack(
            title="Bug Bite",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
