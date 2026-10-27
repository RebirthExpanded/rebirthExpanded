"""Joltik (RSV10PT5 33 -- JP SV11W 030; English WHT/116, WHT/33). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6826ed53-7932-54f7-be03-7580e9e587a8",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    display_name="Joltik",
    searchable_by=["Joltik", "Basic"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=595,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
