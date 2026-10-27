"""Misty's Staryu (SV10 46 -- JP SV9a 023; English DRI/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d31343e6-aa91-58e3-b8ec-2c1b01087cef",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStaryu.Name",
    display_name="Misty's Staryu",
    searchable_by=["Misty's Staryu", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=120,
    abilities=[
        Attack(
            title="Bubble Beam",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
