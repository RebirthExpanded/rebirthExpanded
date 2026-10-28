"""Glimmet (SV3 121 -- JP SV3 063; English OBF/121). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="a5c2c72e-58d3-5827-8d41-35043d279fd3",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    display_name="Glimmet",
    searchable_by=["Glimmet", "Basic"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=969,
    abilities=[
        Attack(
            title="Iron Defense",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=pc.flip_protection(prevent=True),
        ),
        Attack(
            title="Hang Down",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
