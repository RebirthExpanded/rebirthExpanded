"""Hisuian Zorua (ME6A 98 -- JP M6a 098; English 30C/122, 30C/145). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="9f8cad36-c62a-56a9-a1d2-16c845715270",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZorua.Name",
    display_name="Hisuian Zorua",
    searchable_by=["Hisuian Zorua", "Basic"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=570,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
