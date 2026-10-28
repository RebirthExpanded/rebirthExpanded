"""Nickit (SV4 119 -- JP SV3a 040; English PAR/119). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="52e76094-f9a8-5bc7-aa46-a6c8a1944a7f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    display_name="Nickit",
    searchable_by=["Nickit", "Basic"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=827,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
