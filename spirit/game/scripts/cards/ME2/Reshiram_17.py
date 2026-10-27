"""Reshiram (ME2 17 -- JP M2 017; English PFL/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="cb77f004-2bd9-5a15-ab45-e39f8be3ac2c",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiram.Name",
    display_name="Reshiram",
    searchable_by=["Reshiram", "Basic"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Burning Flare",
            game_text="This Pokémon also does 60 damage to itself.",
            cost={PokemonTypes.FIRE: 4},
            damage=240,
            effect=ac.recoil_attack(60),
        ),
    ],
)
