"""Team Rocket's Nidoran♀ (SV10 114 -- JP SV10 058; English DRI/114). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ad1703f6-f154-5ebc-9fdd-a4bb114f43ff",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidoranFemale.Name",
    display_name="Team Rocket's Nidoran♀",
    searchable_by=["Team Rocket's Nidoran♀", "Basic"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=29,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
