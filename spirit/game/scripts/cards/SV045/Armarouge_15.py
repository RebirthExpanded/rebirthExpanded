"""Armarouge (SV045 15 -- JP SV1S 012; English PAF/115, PAF/15, SVI/203, SVI/41). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _fire_off_condition(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return board.active_pokemon(player_id) is not None and bool(bench) and any(
        is_energy_of_type(e, PokemonTypes.FIRE) for p in bench.children for e in p.children)


async def fire_off(ctx):
    active = ctx.board.active_pokemon(ctx.player_id)
    pool = [e for p in ctx.my_bench() for e in ctx.attached_energies(p) if is_energy_of_type(e, PokemonTypes.FIRE)]
    if active is None or not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Fire Energy to move to your Active Pokémon")
    if picks:
        await ctx.move_energy(picks[0], active)


card = PokemonCardDef(
    guid="8642f041-a1a4-542b-a7c7-833083b53b66",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarouge.Name",
    display_name="Armarouge",
    searchable_by=["Armarouge", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Ability(
            title="Fire Off",
            game_text="As often as you like during your turn, you may move a Fire Energy from 1 of your Benched Pokémon to your Active Pokémon.",
            activation=Activations.UNLIMITED,
            condition=_fire_off_condition,
            effect=fire_off,
        ),
        Attack(
            title="Flame Cannon",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
    ],
)
