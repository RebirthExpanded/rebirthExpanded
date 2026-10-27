"""Revavroom (SV07 109 -- JP SVI 043; English SCR/109). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="24bfa879-09ef-5152-8046-fc5cc3adee94",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroom.Name",
    display_name="Revavroom",
    searchable_by=["Revavroom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=109,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    abilities=[
        Attack(
            title="Outta-Control Dash",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
