"""Oshawott (RSV10PT5 21 -- JP SV11W 018; English WHT/105, WHT/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="7cb7f208-acb1-56c3-93d8-ad7f1f3f6c1a",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oshawott.Name",
    display_name="Oshawott",
    searchable_by=["Oshawott", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=501,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Water Gun",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)
