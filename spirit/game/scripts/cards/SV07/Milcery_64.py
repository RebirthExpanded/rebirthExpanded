"""Milcery (SV07 64 -- JP SV7 043; English SCR/152, SCR/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="96bb1766-c92b-5069-a3d7-320d12054868",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    display_name="Milcery",
    searchable_by=["Milcery", "Basic"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=868,
    abilities=[
        Attack(
            title="Mumble",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
