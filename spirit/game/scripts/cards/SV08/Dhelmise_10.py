"""Dhelmise (SV08 10 -- JP SV7a 004; English SSP/10). Japanese art.
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

from spirit.game.session.effects import is_pokemon_card


async def rescue_kedge(ctx):
    pool = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose up to 2 Pokémon")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="0fac9a67-3ffa-5b47-804b-c7bbb614aca6",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name",
    display_name="Dhelmise",
    searchable_by=["Dhelmise", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=781,
    abilities=[
        Attack(
            title="Rescue Kedge",
            game_text="Put up to 2 Pokémon from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=rescue_kedge,
        ),
        Attack(
            title="Annihilating Anchor",
            game_text="Before doing damage, discard all Pokémon Tools from your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=_strip_tools_then_hit,
        ),
    ],
)
