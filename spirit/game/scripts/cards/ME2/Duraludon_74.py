"""Duraludon (ME2 74 -- JP M2 062; English PFL/74). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5f5068e3-a137-55a0-b7fc-db9e6ee83aa0",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    display_name="Duraludon",
    searchable_by=["Duraludon", "Basic"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=884,
    abilities=[
        Attack(
            title="Hyper Beam",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 3},
            damage=70,
            effect=ac.discard_opponent_energy_attack(1),
        ),
    ],
)
