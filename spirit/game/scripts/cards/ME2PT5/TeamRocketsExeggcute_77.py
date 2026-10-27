"""Team Rocket's Exeggcute (ME2PT5 77 -- JP M2a 061; English ASC/77). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="06fe81a0-5e94-5d30-8328-43e06a63e09c",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsExeggcute.Name",
    display_name="Team Rocket's Exeggcute",
    searchable_by=["Team Rocket's Exeggcute", "Basic"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=102,
    abilities=[
        Attack(
            title="Focused Wish",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
