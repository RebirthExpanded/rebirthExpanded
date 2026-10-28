"""Capsakid (SV3 23 -- JP SV3 009; English OBF/23). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="8b914869-6516-51a1-98a6-ed2e21e1df54",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    display_name="Capsakid",
    searchable_by=["Capsakid", "Basic"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=951,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
