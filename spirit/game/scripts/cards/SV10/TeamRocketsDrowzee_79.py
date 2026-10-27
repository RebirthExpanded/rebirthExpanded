"""Team Rocket's Drowzee (SV10 79 -- JP SV10 037; English DRI/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="94403399-2f89-572d-967b-f07c6f991ef5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDrowzee.Name",
    display_name="Team Rocket's Drowzee",
    searchable_by=["Team Rocket's Drowzee", "Basic"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=96,
    abilities=[
        Attack(
            title="Hypnotic Ray",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
