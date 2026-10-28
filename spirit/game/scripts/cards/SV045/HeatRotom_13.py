"""Heat Rotom (SV045 13 -- JP SVEL 003; English PAF/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="bb99b55f-7ec5-578b-a35c-c7bab8e9662c",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatRotom.Name",
    display_name="Heat Rotom",
    searchable_by=["Heat Rotom", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=479,
    abilities=[
        Attack(
            title="Heat Tackle",
            game_text="This Pokémon also does 40 damage to itself.",
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            effect=ac.recoil_attack(40),
        ),
    ],
)
