"""Inkay (SV3 137 -- JP SV3 075; English OBF/137). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="a34e603c-372f-5a8d-9ffd-3ef44cea3551",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay", "Basic"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=686,
    abilities=[
        Attack(
            title="Hug",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
