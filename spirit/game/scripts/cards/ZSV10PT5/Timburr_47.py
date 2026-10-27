"""Timburr (ZSV10PT5 47 -- JP SV11B 050; English BLK/125, BLK/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="83cc5b4c-d7f5-59ad-9ccc-082707d17c3d",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name",
    display_name="Timburr",
    searchable_by=["Timburr", "Basic"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=532,
    abilities=[
        Attack(
            title="Low Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Strength",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
