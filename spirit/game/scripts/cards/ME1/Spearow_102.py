"""Spearow (ME1 102 -- JP M1L 052; English MEG/102, MEG/151). Japanese art.
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
    guid="4947a7b9-367b-5c25-bec0-09f8e3117f43",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    display_name="Spearow",
    searchable_by=["Spearow", "Basic"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=21,
    abilities=[
        Attack(
            title="Pluck",
            game_text="Before doing damage, discard all Pokémon Tools from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_strip_tools_then_hit,
        ),
    ],
)
