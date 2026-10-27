"""Klinklang (SV07 101 -- JP SV7 069; English SCR/101). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_stage2_pokemon
from spirit.game.session.passives import effective_bench_capacity


def _rotation_condition(board, player_id, pokemon=None) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    bench = board.find_player_area(player_id, "bench")
    return (other is not None and any(is_stage2_pokemon(p) for p in board.pokemon_in_play(other))
            and len(bench.children if bench else []) < effective_bench_capacity(board, player_id))


async def emergency_rotation(ctx):
    await ctx.bench_pokemon(ctx.source)


card = PokemonCardDef(
    guid="05c6b356-8e81-5e18-bd05-e8c359403135",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=101,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Ability(
            title="Emergency Rotation",
            game_text="Once during your turn, if this Pokémon is in your hand and your opponent has any Stage 2 Pokémon in play, you may put this Pokémon onto your Bench.",
            usable_from="hand",
            activation=Activations.ONCE_PER_TURN,
            condition=_rotation_condition,
            effect=emergency_rotation,
        ),
        Attack(
            title="Hyper Ray",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=ac.self_energy_discard_attack(all_energy=True),
        ),
    ],
)
