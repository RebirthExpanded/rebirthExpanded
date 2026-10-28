"""Crocalor (SV2 36 -- JP SV1a 019; English PAL/202, PAL/36, SVP/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="201910c7-9cc5-53c1-8d7c-486e69ca7b57",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    display_name="Crocalor",
    searchable_by=["Crocalor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name",
    family_id=909,
    abilities=[
        Attack(
            title="Steady Firebreathing",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Hyper Voice",
            game_text="",
            cost={PokemonTypes.FIRE: 2},
            damage=70,
        ),
    ],
)
