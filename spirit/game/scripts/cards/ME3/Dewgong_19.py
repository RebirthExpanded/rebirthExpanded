"""Dewgong (ME3 19 -- JP M3 019; English POR/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)



def _can_wash(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return board.active_pokemon(player_id) is not None and any(
        is_energy_of_type(e, PokemonTypes.WATER) for p in (bench.children if bench else []) for e in board.attached_energies(p))


async def wash_out(ctx):
    active = ctx.my_active()
    pool = [e for p in ctx.my_bench() for e in ctx.attached_energies(p) if is_energy_of_type(e, PokemonTypes.WATER)]
    if active is None or not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Choose a Water Energy to move to your Active Pokémon")
    if picks:
        await ctx.move_energy(picks[0], active)


card = PokemonCardDef(
    guid="0697dbe7-4f97-590f-9562-e90c957b0cae",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong",
    searchable_by=["Dewgong", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Ability(
            title="Wash Out",
            game_text="As often as you like during your turn, you may use this Ability. Move a Water Energy from 1 of your Benched Pokémon to your Active Pokémon.",
            activation=Activations.UNLIMITED,
            condition=_can_wash,
            effect=wash_out,
        ),
        Attack(
            title="Wave Splash",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=60,
        ),
    ],
)
