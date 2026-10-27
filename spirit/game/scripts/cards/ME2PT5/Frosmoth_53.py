"""Frosmoth (ME2PT5 53 -- JP M2a 041; English ASC/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _alluring_condition(board, player_id, pokemon) -> bool:
    return board.active_pokemon(player_id) is pokemon


async def alluring_wings(ctx):
    await ctx.draw_cards(1)
    await ctx.draw_cards(1, player_id=ctx.opponent_id)


async def cold_cyclone(ctx):
    await ctx.deal_damage()
    pool = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.WATER)]
    bench = ctx.my_bench()
    if not pool or not bench or ctx.attacker in ctx.knockouts:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Water Energy to move")
    dest = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move it to") if picks else None
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


card = PokemonCardDef(
    guid="0fd7f53d-a69e-59e0-8bc0-c41a02da24e3",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frosmoth.Name",
    display_name="Frosmoth",
    searchable_by=["Frosmoth", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    family_id=872,
    abilities=[
        Ability(
            title="Alluring Wings",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may use this Ability. Each player draws a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=_alluring_condition,
            effect=alluring_wings,
        ),
        Attack(
            title="Cold Cyclone",
            game_text="Move a Water Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=90,
            effect=cold_cyclone,
        ),
    ],
)
