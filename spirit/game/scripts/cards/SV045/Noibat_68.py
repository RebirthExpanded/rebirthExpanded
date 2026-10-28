"""Noibat (SV045 68 -- JP SV2D 057; English PAF/194, PAF/68, PAL/152). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c9ba818f-4d94-59a4-b5d0-65a4cf82bada",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    display_name="Noibat",
    searchable_by=["Noibat", "Basic"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=714,
    abilities=[
        Attack(
            title="Gust",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
    ],
)
