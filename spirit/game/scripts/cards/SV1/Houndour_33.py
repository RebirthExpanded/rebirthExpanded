"""Houndour (SV1 33 -- JP SV1V 017; English SVI/33). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="0f7e694f-d569-547e-928c-5c1caf9e81ca",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    display_name="Houndour",
    searchable_by=["Houndour", "Basic"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=228,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Flare",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
