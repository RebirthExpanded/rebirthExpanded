"""Salandit (SV3 139 -- JP SV1a 060; English OBF/139). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="4726951a-9c48-5f19-8420-40f241a8054c",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    display_name="Salandit",
    searchable_by=["Salandit", "Basic"],
    subtypes=["Basic"],
    collector_number=139,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=757,
    abilities=[
        Attack(
            title="Suffocating Gas",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
