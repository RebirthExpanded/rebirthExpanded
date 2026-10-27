"""Linoone (ME2 82 -- JP M2 070; English PFL/82). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


def _mega_ex(pokemon) -> bool:
    subs = subtypes_for(pokemon.archetype_id) or []
    return "SV_Mega" in subs and "ex" in subs


def _excited_dash_condition(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return (bench is not None and pokemon.parent is bench
            and any(_mega_ex(p) for p in board.pokemon_in_play(player_id)))


async def excited_dash(ctx):
    await ctx.switch_active(ctx.player_id, ctx.source)


card = PokemonCardDef(
    guid="e94f28d6-f468-5f5e-bf76-6cc2b5960e7f",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Linoone.Name",
    display_name="Linoone",
    searchable_by=["Linoone", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    family_id=263,
    abilities=[
        Ability(
            title="Excited Dash",
            game_text="Once during your turn, if this Pokémon is on your Bench, and if you have any Mega Evolution Pokémon ex in play, you may use this Ability. Switch this Pokémon with your Active Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_excited_dash_condition,
            effect=excited_dash,
        ),
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
