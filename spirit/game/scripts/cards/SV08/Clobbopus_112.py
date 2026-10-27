"""Clobbopus (SV08 112 -- JP SV7a 032; English SSP/112, SSP/207). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="1513a6ab-11e8-5f80-9c7d-d0ec8ab07103",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    display_name="Clobbopus",
    searchable_by=["Clobbopus", "Basic"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=852,
    abilities=[
        Attack(
            title="Slight Intrusion",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
