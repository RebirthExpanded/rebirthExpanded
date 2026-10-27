"""Pawniard (ZSV10PT5 64 -- JP SV11B 066; English BLK/142, BLK/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="4a0bc8a6-8d79-5e4e-94e5-f8ef3cfe169a",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    display_name="Pawniard",
    searchable_by=["Pawniard", "Basic"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=624,
    abilities=[
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
