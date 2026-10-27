"""Murkrow (MF 18 -- JP MF 018; English 30C/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="3ff845a3-3d65-5587-9264-2d09f6c095ba",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    display_name="Murkrow",
    searchable_by=["Murkrow", "Basic"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=198,
    abilities=[
        Attack(
            title="Clumsily Clutch",
            game_text="Flip a coin. If heads, during your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=ac.condition_attack(flip=True, no_retreat=True),
        ),
    ],
)
