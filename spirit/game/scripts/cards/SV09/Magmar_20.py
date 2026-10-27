"""Magmar (SV09 20 -- JP SV9 013; English JTG/20). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ce3edb9e-48b0-5c8c-86ad-029c37906afe",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=240,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.BURNED, flip=True),
        ),
    ],
)
