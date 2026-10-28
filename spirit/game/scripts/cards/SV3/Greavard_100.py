"""Greavard (SV3 100 -- JP SV3 053; English OBF/100). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="80d8492d-def7-5330-8025-ea6f4989c6ab",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    display_name="Greavard",
    searchable_by=["Greavard", "Basic"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=971,
    abilities=[
        Attack(
            title="Play Rough",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
    ],
)
