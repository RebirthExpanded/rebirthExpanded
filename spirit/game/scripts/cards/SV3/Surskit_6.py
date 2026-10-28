"""Surskit (SV3 6 -- JP SV2P 001; English OBF/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="82ff41f8-5101-5d30-aaa4-c842523efc8d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    display_name="Surskit",
    searchable_by=["Surskit", "Basic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=283,
    abilities=[
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
