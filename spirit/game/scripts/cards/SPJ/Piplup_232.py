"""Piplup (SPJ 232 -- JP SP 232; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="1c8c15d6-b9f4-5727-8f47-91c2c0771ef8",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    display_name="Piplup",
    searchable_by=["Piplup", "Basic"],
    subtypes=["Basic"],
    collector_number=232,
    set_code="SPJ",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=393,
    abilities=[
        Attack(
            title="Do Your Best",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
    ],
)
