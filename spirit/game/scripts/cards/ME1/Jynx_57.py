"""Jynx (ME1 57 -- JP M1S 039; English MEG/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b7d01c7c-ce92-57c0-a88e-2ceb3da83560",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=238,
    abilities=[
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 30, base=30),
        ),
    ],
)
