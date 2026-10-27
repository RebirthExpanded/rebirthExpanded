"""Cherubi (MF 2 -- JP MF 002; English 30C/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="4b77b7d5-0c3c-5136-b405-fabb7bb6c194",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    display_name="Cherubi",
    searchable_by=["Cherubi", "Basic"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=420,
    abilities=[
        Attack(
            title="Hide",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Flop",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
