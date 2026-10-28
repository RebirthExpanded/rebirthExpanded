"""Gible (SV4 94 -- JP SV3a 027; English PAR/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="25b228af-7d0a-58d0-8a38-930b0b482aa6",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    display_name="Gible",
    searchable_by=["Gible", "Basic"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=443,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
