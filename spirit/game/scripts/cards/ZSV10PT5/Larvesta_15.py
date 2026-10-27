"""Larvesta (ZSV10PT5 15 -- JP SV11B 018; English BLK/15, BLK/99). Japanese art.
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
    guid="1ef9e353-3ab6-5d92-85a6-848d25abd2da",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    display_name="Larvesta",
    searchable_by=["Larvesta", "Basic"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=636,
    abilities=[
        Attack(
            title="Peck Off",
            game_text="Before doing damage, discard all Pokémon Tools from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_strip_tools_then_hit,
        ),
    ],
)
