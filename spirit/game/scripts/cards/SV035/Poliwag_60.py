"""Poliwag (SV035 60 -- JP SV2a 060; English MEW/60). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="eb7c022e-dfba-5fa3-b4ca-3a3658ab2b69",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name",
    display_name="Poliwag",
    searchable_by=["Poliwag", "Basic"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=60,
    abilities=[
        Attack(
            title="Bubble",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
