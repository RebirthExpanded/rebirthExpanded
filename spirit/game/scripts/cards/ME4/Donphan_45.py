"""Donphan (ME4 45 -- JP M4 045; English CRI/45). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="513f0a61-04b7-51c9-a90a-16328df38abf",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Attack(
            title="No Reprieve",
            game_text="During your next turn, attacks used by this Pokémon do 120 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=pc.boost_own_next_turn(120),
        ),
        Attack(
            title="Smashing Headbutt",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
