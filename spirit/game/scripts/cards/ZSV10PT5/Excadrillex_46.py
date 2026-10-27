"""Excadrill ex (ZSV10PT5 46 -- JP SV11B 049; English BLK/160, BLK/168, BLK/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def piercing_drill(ctx):
    await ctx.deal_damage()
    pool = [p for p in ctx.opponent_bench() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's damaged Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(60, target=target)


async def rock_tumble(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="95ce7bff-7412-5899-9ad4-357615e6986b",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Excadrillex.Name",
    display_name="Excadrill ex",
    searchable_by=["Excadrill ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=46,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    family_id=529,
    abilities=[
        Attack(
            title="Piercing Drill",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            effect=piercing_drill,
        ),
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=200,
            effect=rock_tumble,
        ),
    ],
)
