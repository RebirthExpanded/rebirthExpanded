"""Zekrom (SV4 66 -- JP SV3a 018; English PAR/66). Japanese art.
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
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c73f2722-18c1-572c-870f-9b9728429c88",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name",
    display_name="Zekrom",
    searchable_by=["Zekrom", "Basic"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Crushing Short",
            game_text="Before doing damage, discard all Pokémon Tools from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_strip_tools_then_hit,
        ),
        Attack(
            title="Raging Thunder",
            game_text="This attack also does 40 damage to 1 of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ac.snipe_attack(40, pool="bench", side="mine", also_base=True),
        ),
    ],
)
