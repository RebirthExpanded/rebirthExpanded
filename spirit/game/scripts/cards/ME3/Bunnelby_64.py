"""Bunnelby (ME3 64 -- JP M3 063; English POR/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e2be0bb7-b0df-56cc-b2f3-7ad880d4cc30",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name",
    display_name="Bunnelby",
    searchable_by=["Bunnelby", "Basic"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=659,
    abilities=[
        Attack(
            title="Smash Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
