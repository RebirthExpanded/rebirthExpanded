"""Spewpa (SV08 6 -- JP SV8 005; English SSP/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="b892b230-a31c-584d-9586-926b0a80b449",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    display_name="Spewpa",
    searchable_by=["Spewpa", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name",
    family_id=664,
    abilities=[
        Attack(
            title="Wander About",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.switch_self_attack(),
        ),
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)
