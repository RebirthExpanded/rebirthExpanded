"""Cetoddle (SV1 59 -- JP SV1V 024; English SVI/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="f2bb7e4e-b83f-579d-ba5d-b4d8f148cabf",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    display_name="Cetoddle",
    searchable_by=["Cetoddle", "Basic"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=974,
    abilities=[
        Attack(
            title="Icicle",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Sharp Fin",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
