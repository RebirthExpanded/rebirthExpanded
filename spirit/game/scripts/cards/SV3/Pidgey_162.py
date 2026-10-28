"""Pidgey (SV3 162 -- JP SV3 087; English OBF/162, OBF/207). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="cd76cba1-344c-5059-ba02-7f619fac1600",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    display_name="Pidgey",
    searchable_by=["Pidgey", "Basic"],
    subtypes=["Basic"],
    collector_number=162,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=16,
    abilities=[
        Attack(
            title="Gust",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
