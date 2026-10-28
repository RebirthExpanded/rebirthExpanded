"""Sandygast (SV2 95 -- JP SV2D 029; English PAL/214, PAL/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="5f4e1f2b-0c15-5a7b-a5d1-bb9793a2a8cf",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    display_name="Sandygast",
    searchable_by=["Sandygast", "Basic"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=769,
    abilities=[
        Attack(
            title="Mumble",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Mud Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
