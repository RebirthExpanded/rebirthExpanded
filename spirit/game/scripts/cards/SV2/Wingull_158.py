"""Wingull (SV2 158 -- JP SV2P 058; English PAF/203, PAL/158). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="59dca6ba-f5cb-5cdb-8fdf-056558169a53",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    display_name="Wingull",
    searchable_by=["Wingull", "Basic"],
    subtypes=["Basic"],
    collector_number=158,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=278,
    abilities=[
        Attack(
            title="Gust",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
