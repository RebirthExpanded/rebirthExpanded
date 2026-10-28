"""Charmander (SV3 26 -- JP SV3 012; English OBF/26, SVP/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="8027abdc-0fbc-513e-9183-c6583d71bc5c",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Heat Tackle",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
