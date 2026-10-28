"""Nymble (SV2 20 -- JP SV1a 009; English PAL/20). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="601a0439-1ebe-56d8-b8ef-151f7b4df1a2",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name",
    display_name="Nymble",
    searchable_by=["Nymble", "Basic"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=919,
    abilities=[
        Attack(
            title="Wild Kick",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
