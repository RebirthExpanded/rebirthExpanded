"""Oshawott (MEP 51 -- JP MP 115; English MEP/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="99ea3b2e-a999-56eb-9efa-c0ac33b0f76f",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oshawott.Name",
    display_name="Oshawott",
    searchable_by=["Oshawott", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=501,
    abilities=[
        Attack(
            title="Razor Shell",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
    ],
)
