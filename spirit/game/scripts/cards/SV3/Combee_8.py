"""Combee (SV3 8 -- JP SV3 006; English OBF/8). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def share(ctx):
    pool = [p for p in ctx.my_bench() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Pokémon to heal 20 damage from")
        if target is not None:
            await ctx.heal(20, target)


card = PokemonCardDef(
    guid="d5ecdd28-b559-50c3-8c30-f9f9d30b588a",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    display_name="Combee",
    searchable_by=["Combee", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=415,
    abilities=[
        Attack(
            title="Share",
            game_text="Heal 20 damage from 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=share,
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
        ),
    ],
)
