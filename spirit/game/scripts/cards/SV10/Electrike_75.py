"""Electrike (SV10 75 -- JP SV9a 037; English DRI/196, DRI/75). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="48a0e0c9-9b9c-5e74-9dfa-c2bc54ee1a66",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    display_name="Electrike",
    searchable_by=["Electrike", "Basic"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=309,
    abilities=[
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Tiny Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
