"""Arboliva (MEM 8 -- JP MEM 008; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


def _opp_bench(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    bench = board.find_player_area(other, "bench") if other else None
    return bool(bench and bench.children)


card = PokemonCardDef(
    guid="ed807e64-13e7-55ad-bc4a-3ca2ffcba1a1",
    key="MEM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arboliva.Name",
    display_name="Arboliva",
    searchable_by=["Arboliva", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="MEM",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    family_id=928,
    abilities=[
        Ability(
            title="Oil Slip",
            game_text="Once during your turn, you may use this Ability. Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            activation=Activations.ONCE_PER_TURN,
            condition=_opp_bench,
            effect=su.opponent_switches,
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=su.heal_attack(30),
        ),
    ],
)
