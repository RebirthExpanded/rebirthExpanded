"""Purrloin (MEZ 4 -- JP MEZ 004; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="52409c31-0408-5aa3-8370-054062ffe93c",
    key="MEZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    display_name="Purrloin",
    searchable_by=["Purrloin", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="MEZ",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=509,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)
