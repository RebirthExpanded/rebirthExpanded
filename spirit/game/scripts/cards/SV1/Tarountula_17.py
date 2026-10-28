"""Tarountula (SV1 17 -- JP SV1V 006; English SVI/17, SVI/199). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9e7e9ac6-9c35-5f3a-99f0-82df36d1509f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name",
    display_name="Tarountula",
    searchable_by=["Tarountula", "Basic"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=917,
    abilities=[
        Attack(
            title="String Shot",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
