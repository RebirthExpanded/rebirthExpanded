"""Tadbulb (SV2 77 -- JP SV2D 023; English PAL/77). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c9634fda-266d-574a-85ae-cfcedc9e6a11",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    display_name="Tadbulb",
    searchable_by=["Tadbulb", "Basic"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=938,
    abilities=[
        Attack(
            title="Thunder Wave",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
