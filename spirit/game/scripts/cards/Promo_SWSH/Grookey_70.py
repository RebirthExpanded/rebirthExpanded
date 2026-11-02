"""Grookey (Promo_SWSH 70 -- JP SP 007; English SP/70). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="334c68f6-a90a-5ef2-acf4-7d3fda622bbd",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name",
    display_name="Grookey",
    searchable_by=["Grookey", "Basic"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=810,
    abilities=[
        Attack(
            title="Full On",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
