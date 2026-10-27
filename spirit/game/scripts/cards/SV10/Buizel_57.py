"""Buizel (SV10 57 -- JP SV9a 030; English DRI/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="9023f562-594a-5426-b1d4-5da8d868db0b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    display_name="Buizel",
    searchable_by=["Buizel", "Basic"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=418,
    abilities=[
        Attack(
            title="Tail Whap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Wave Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
