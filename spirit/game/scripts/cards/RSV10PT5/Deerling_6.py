"""Deerling (RSV10PT5 6 -- JP SV11W 006; English WHT/6, WHT/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e2214e4d-723a-5727-b14b-c8c94a681b04",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name",
    display_name="Deerling",
    searchable_by=["Deerling", "Basic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=585,
    abilities=[
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
