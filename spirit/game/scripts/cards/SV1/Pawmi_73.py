"""Pawmi (SV1 73 -- JP SV1V 033; English SVI/73). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9d7d1f54-975a-562c-be74-1a8ded6d5b24",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name",
    display_name="Pawmi",
    searchable_by=["Pawmi", "Basic"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=921,
    abilities=[
        Attack(
            title="Jolt",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
