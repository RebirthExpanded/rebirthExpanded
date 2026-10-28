"""Palpitoad (SV3 51 -- JP SV3 024; English OBF/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="a9ba889e-a2bd-58fe-842b-1cd5eaf9209b",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    display_name="Palpitoad",
    searchable_by=["Palpitoad", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Rain Splash",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=50,
        ),
    ],
)
