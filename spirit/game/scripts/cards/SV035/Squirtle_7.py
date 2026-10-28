"""Squirtle (SV035 7 -- JP SV2a 007; English MEW/170, MEW/7, SCR/148). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="8db92070-82fe-5aaf-8679-7d84adb4db78",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    display_name="Squirtle",
    searchable_by=["Squirtle", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=7,
    abilities=[
        Attack(
            title="Withdraw",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.WATER: 1},
            effect=pc.flip_protection(prevent=True),
        ),
        Attack(
            title="Skull Bash",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=20,
        ),
    ],
)
