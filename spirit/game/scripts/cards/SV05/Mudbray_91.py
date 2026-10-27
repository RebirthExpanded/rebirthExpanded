"""Mudbray (SV05 91 -- JP SV5K 037; English TEF/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="2ed49880-6bd7-5c6c-8ebe-fdf23e68289b",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name",
    display_name="Mudbray",
    searchable_by=["Mudbray", "Basic"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=749,
    abilities=[
        Attack(
            title="Smash Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Mud-Slap",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
