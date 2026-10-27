"""Team Rocket's Houndour (SV10 37 -- JP SV10 016; English DRI/37). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="fc1f5bc8-49e8-5c5b-ac75-2318700cd157",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsHoundour.Name",
    display_name="Team Rocket's Houndour",
    searchable_by=["Team Rocket's Houndour", "Basic"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=228,
    abilities=[
        Attack(
            title="Steady Firebreathing",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
