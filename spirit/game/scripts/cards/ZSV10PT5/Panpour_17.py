"""Panpour (ZSV10PT5 17 -- JP SV11B 020; English BLK/101, BLK/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="39746d67-2ac4-5334-a72e-88d05cbbe5cf",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name",
    display_name="Panpour",
    searchable_by=["Panpour", "Basic"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=515,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
