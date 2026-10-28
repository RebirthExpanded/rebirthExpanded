"""Blipbug (SV4 10 -- JP SV4M 003; English PAR/10). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="702fc58a-2b85-5ce8-a5b6-3ac594858213",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blipbug.Name",
    display_name="Blipbug",
    searchable_by=["Blipbug", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=824,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
