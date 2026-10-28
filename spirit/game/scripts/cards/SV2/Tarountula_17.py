"""Tarountula (SV2 17 -- JP SV2D 008; English PAL/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c707b49f-29fd-5288-9a13-d1c0e56bfdcb",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name",
    display_name="Tarountula",
    searchable_by=["Tarountula", "Basic"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=917,
    abilities=[
        Attack(
            title="Hook",
            game_text="",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
        ),
    ],
)
