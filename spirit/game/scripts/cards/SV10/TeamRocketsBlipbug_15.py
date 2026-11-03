"""Team Rocket's Blipbug (SV10 15 -- JP SV10 007; English DRI/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.sm3 import code_check


card = PokemonCardDef(
    guid="fbe13fe0-3817-55e8-82b9-bd0b1b62bfb1",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsBlipbug.Name",
    display_name="Team Rocket's Blipbug",
    searchable_by=["Team Rocket's Blipbug", "Basic"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=824,
    abilities=[
        Attack(
            title="Searching Eyes",
            game_text="Look at 1 of your opponent's face-down Prize cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=code_check,
        ),
    ],
)
