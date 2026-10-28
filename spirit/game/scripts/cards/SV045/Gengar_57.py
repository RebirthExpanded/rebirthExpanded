"""Gengar (SV045 57 -- JP SV3a 035; English PAF/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _gate_condition(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return bool(bench and bench.children) and board.active_pokemon(player_id) is not None


async def night_gate(ctx):
    bench = ctx.my_bench()
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with your Active Pokémon") if bench else None
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="6ec6c3cb-82ef-51aa-b291-f1e9fb6edba7",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=57,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Night Gate",
            game_text="Once during your turn, you may switch your Active Pokémon with 1 of your Benched Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_gate_condition,
            effect=night_gate,
        ),
        Attack(
            title="Nightmare",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
