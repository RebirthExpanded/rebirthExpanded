"""N's Joltik (SV09 49 -- JP SV9 028; English JTG/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions

from spirit.game.session.effects import is_pokemon_tool


async def _strip_tools(ctx) -> int:
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return 0
    tools = [c for c in target.children if is_pokemon_tool(c)]
    if tools:
        await ctx.discard_cards(tools)
    return len(tools)


async def _strip_tools_then_hit(ctx):
    await _strip_tools(ctx)
    await ctx.deal_damage()


async def zapping_short(ctx):
    stripped = await _strip_tools(ctx)
    if stripped:
        target = ctx.opponent_active()
        if target is not None:
            await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="b16d8854-c1fc-503b-83b7-b1c68b40c035",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsJoltik.Name",
    display_name="N's Joltik",
    searchable_by=["N's Joltik", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=595,
    abilities=[
        Attack(
            title="Zapping Short",
            game_text="Before doing damage, discard all Pokémon Tools from your opponent's Active Pokémon. If you discarded a Pokémon Tool in this way, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=zapping_short,
        ),
    ],
)
