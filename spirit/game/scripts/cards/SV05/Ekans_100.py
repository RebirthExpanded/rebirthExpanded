"""Ekans (SV05 100 -- JP SV5K 043; English TEF/100). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="55f8c6c1-5a5c-56b9-90d7-4edb06c1af22",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    display_name="Ekans",
    searchable_by=["Ekans", "Basic"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=23,
    abilities=[
        Attack(
            title="Poison Blend",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused and Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
        ),
    ],
)
