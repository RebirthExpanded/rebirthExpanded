"""Simipour (ZSV10PT5 18 -- JP SV11B 021; English BLK/102, BLK/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="222641fe-7ccf-58ab-9ab5-be81f4f387d5",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simipour.Name",
    display_name="Simipour",
    searchable_by=["Simipour", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name",
    family_id=515,
    abilities=[
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
