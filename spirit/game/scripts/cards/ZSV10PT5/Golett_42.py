"""Golett (ZSV10PT5 42 -- JP SV11B 045; English BLK/122, BLK/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="04d3ae9f-1e5c-593d-a9e8-a5475b3e1e0e",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    display_name="Golett",
    searchable_by=["Golett", "Basic"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=622,
    abilities=[
        Attack(
            title="Best Punch",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
