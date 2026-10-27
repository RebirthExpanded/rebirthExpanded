"""Darumaka (ZSV10PT5 13 -- JP SV11B 013; English BLK/13, BLK/97). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="3c79d830-778f-5996-8017-659c1d649757",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    display_name="Darumaka",
    searchable_by=["Darumaka", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=554,
    abilities=[
        Attack(
            title="Will-O-Wisp",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
