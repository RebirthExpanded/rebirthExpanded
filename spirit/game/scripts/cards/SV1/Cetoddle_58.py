"""Cetoddle (SV1 58 -- JP SV1V 023; English SVI/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="65a356c4-175c-58ea-98a5-825e82465048",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    display_name="Cetoddle",
    searchable_by=["Cetoddle", "Basic"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=974,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
