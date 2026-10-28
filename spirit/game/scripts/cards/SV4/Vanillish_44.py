"""Vanillish (SV4 44 -- JP SV4M 018; English PAR/190, PAR/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="393cdebc-13f5-54c5-8007-419f5da29155",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    display_name="Vanillish",
    searchable_by=["Vanillish", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Frost Smash",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=60,
        ),
    ],
)
