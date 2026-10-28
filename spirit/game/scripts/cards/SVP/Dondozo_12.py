"""Dondozo (SVP 12 -- JP SVG 019; English SVP/12). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9ccd1836-d945-54fb-8fd1-12eaa676ae97",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dondozo.Name",
    display_name="Dondozo",
    searchable_by=["Dondozo", "Basic"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=977,
    abilities=[
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Dangerous Wave",
            game_text="Flip 2 coins. If both of them are heads, this attack does 100 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=ac.flip_damage(coins=2, bonus=100, require_all=True),
        ),
    ],
)
