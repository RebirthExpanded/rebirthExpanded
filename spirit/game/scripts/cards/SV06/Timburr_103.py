"""Timburr (SV06 103 -- JP SV6 059; English TWM/103, TWM/183). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="15f0dd58-309d-5ef1-9402-0cd054d0a373",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name",
    display_name="Timburr",
    searchable_by=["Timburr", "Basic"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=532,
    abilities=[
        Attack(
            title="Best Punch",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
