"""Sprigatito (SV1 13 -- JP SVAM 004; English SVI/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="757a1689-41b8-5147-9c94-0518447e2dbc",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name",
    display_name="Sprigatito",
    searchable_by=["Sprigatito", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=906,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Leafage",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
