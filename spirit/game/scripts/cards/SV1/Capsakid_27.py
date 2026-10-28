"""Capsakid (SV1 27 -- JP SV1V 012; English SVI/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="be4a980d-45db-53b5-9cf1-a56c5d197d86",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    display_name="Capsakid",
    searchable_by=["Capsakid", "Basic"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=951,
    abilities=[
        Attack(
            title="Slightly Spicy",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.BURNED, flip=True),
        ),
    ],
)
