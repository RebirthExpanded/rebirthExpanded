"""Fletchinder (ME3 13 -- JP M3 013; English POR/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="91799b68-f89a-5aea-939b-eee8029abf9c",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    display_name="Fletchinder",
    searchable_by=["Fletchinder", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Flare",
            game_text="",
            cost={PokemonTypes.FIRE: 2},
            damage=60,
        ),
    ],
)
