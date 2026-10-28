"""Froakie (SV3 56 -- JP SVD 027; English OBF/56). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b167a064-de68-5e09-a4cf-cee4da867efe",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name",
    display_name="Froakie",
    searchable_by=["Froakie", "Basic"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=656,
    abilities=[
        Attack(
            title="Try Bouncing",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
