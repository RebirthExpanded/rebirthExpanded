"""Flittle (SV4 80 -- JP SV4M 032; English PAR/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="204be52d-c5b7-5fcf-b2f8-d7d8c1118d83",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    display_name="Flittle",
    searchable_by=["Flittle", "Basic"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=955,
    abilities=[
        Attack(
            title="Psychic",
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 10, base=10),
        ),
    ],
)
