"""Haunter (ME3 49 -- JP M3 048; English POR/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="def1ab6a-6da6-59a0-b122-0d19d2fd0e53",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    display_name="Haunter",
    searchable_by=["Haunter", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Haunt",
            game_text="Place 3 damage counters on your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.place_counters(3),
        ),
    ],
)
