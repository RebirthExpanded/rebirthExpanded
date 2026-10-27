"""Braixen (ME4 12 -- JP M4 012; English CRI/12). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6fdcbb41-4c73-5821-b1c4-57fb1ee61ef1",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    display_name="Braixen",
    searchable_by=["Braixen", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name",
    family_id=653,
    abilities=[
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=80,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
