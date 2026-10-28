"""Liepard (SV4 115 -- JP SV4K 048; English PAR/115). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def dishonest_swap(ctx):
    pool = [p for p in ctx.my_bench() if _counters(ctx.board, p) > 0]
    d = ctx.opponent_active()
    if not pool or d is None:
        return
    source = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Pokémon")
    if source is not None:
        await ctx.move_damage_counters(source, d)


card = PokemonCardDef(
    guid="051520b5-0a58-5a76-8b0b-65868bd73188",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Dishonest Swap",
            game_text="Move all damage counters from 1 of your Benched Pokémon to your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=dishonest_swap,
        ),
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
