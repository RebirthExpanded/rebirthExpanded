"""Whimsicott (MEP 19 -- JP M2 038; English MEP/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def healing_fluff(ctx):
    pool = [p for p in ctx.my_bench() if _counters(ctx.board, p) > 0]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Pokémon to heal all damage from")
    if target is not None:
        await ctx.heal(_counters(ctx.board, target) * 10, target)


card = PokemonCardDef(
    guid="e0c921f6-6a6d-58ad-8c16-e02b3df4008d",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Attack(
            title="Healing Fluff",
            game_text="Heal all damage from 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=healing_fluff,
        ),
        Attack(
            title="U-turn",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            effect=su.switch_self_attack(),
        ),
    ],
)
