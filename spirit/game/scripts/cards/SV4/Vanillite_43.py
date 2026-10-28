"""Vanillite (SV4 43 -- JP SV4M 017; English PAR/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="7a0c75ce-8bdb-5044-9b5d-afb654c74a87",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name",
    display_name="Vanillite",
    searchable_by=["Vanillite", "Basic"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=582,
    abilities=[
        Attack(
            title="Chilly",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=40,
        ),
    ],
)
