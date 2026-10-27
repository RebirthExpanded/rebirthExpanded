"""Arven's Skwovet (SV10 158 -- JP SV9a 054; English DRI/158). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

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


card = PokemonCardDef(
    guid="b2468f5a-cfa3-53cf-96f3-d4e12018adb4",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensSkwovet.Name",
    display_name="Arven's Skwovet",
    searchable_by=["Arven's Skwovet", "Basic"],
    subtypes=["Basic"],
    collector_number=158,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=819,
    abilities=[
        Attack(
            title="Gnaw Through",
            game_text="Before doing damage, discard all Pokémon Tools from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_strip_tools_then_hit,
        ),
    ],
)
