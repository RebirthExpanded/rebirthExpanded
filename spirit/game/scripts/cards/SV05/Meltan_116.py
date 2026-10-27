"""Meltan (SV05 116 -- JP SV5M 049; English TEF/116, TEF/179). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="2cf93316-aabf-59d5-be68-ade8d2b4dac7",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    display_name="Meltan",
    searchable_by=["Meltan", "Basic"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=808,
    abilities=[
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.METAL: 2},
            damage=50,
        ),
    ],
)
