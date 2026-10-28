"""Rockruff (SV3 116 -- JP SV3 061; English OBF/116). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="ec004da5-1a67-59ac-b3fa-a45a3ba63925",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    display_name="Rockruff",
    searchable_by=["Rockruff", "Basic"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=744,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
