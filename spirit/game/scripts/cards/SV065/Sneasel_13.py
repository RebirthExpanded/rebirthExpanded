"""Sneasel (SV065 13 -- JP SV6a 013; English ASC/44, SFA/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="1f8b0adb-5231-5e14-b85d-e60d439694d1",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=215,
    abilities=[
        Attack(
            title="Cut",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Beset",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
