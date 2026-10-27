"""Cascoon (ME2PT5 14 -- JP M2a 007; English ASC/14). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="d48a7326-3ff0-5995-9f9c-e9a4fb488cd4",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    display_name="Cascoon",
    searchable_by=["Cascoon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Trading Places",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=su.switch_self_attack(),
        ),
    ],
)
