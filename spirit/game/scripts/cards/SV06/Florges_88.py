"""Florges (SV06 88 -- JP SV5a 038; English TWM/88). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


def _captivating_condition(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    bench = board.find_player_area(other, "bench") if other else None
    return bool(bench and bench.children)


async def captivating_invitation(ctx):
    results = await ctx.flip_coins(1, "Captivating Invitation")
    bench = ctx.opponent_bench()
    if not (results and results[0]) or not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose the opponent's new Active Pokémon")
    if target is not None and await ctx.switch_active(ctx.opponent_id, target):
        await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="993953bf-1d30-537e-b69f-8636733c87e1",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name",
    display_name="Florges",
    searchable_by=["Florges", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=88,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    family_id=669,
    abilities=[
        Ability(
            title="Captivating Invitation",
            game_text="Once during your turn, you may flip a coin. If heads, switch in 1 of your opponent's Benched Pokémon to the Active Spot, and the new Active Pokémon is now Confused.",
            activation=Activations.ONCE_PER_TURN,
            condition=_captivating_condition,
            effect=captivating_invitation,
        ),
        Attack(
            title="Magical Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
