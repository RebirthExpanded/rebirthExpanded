"""Bewear (SMD 18 -- JP SMD 018; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="fcc9df7e-05ce-5e36-8bba-badae61832e1",
    key="SMD",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="SMD",
    regulation_mark="A",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Attack(
            title="Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Snatch",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=ac.discard_opponent_energy_attack(1),
        ),
    ],
)
