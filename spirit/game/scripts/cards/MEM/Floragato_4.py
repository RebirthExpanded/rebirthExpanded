"""Floragato (MEM 4 -- JP MEM 004; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="3709308e-2da2-5e65-a6f7-52354baea83a",
    key="MEM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    display_name="Floragato",
    searchable_by=["Floragato", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="MEM",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name",
    family_id=906,
    abilities=[
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
        ),
    ],
)
