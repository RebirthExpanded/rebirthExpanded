"""Zamazenta (ME6A 86 -- JP M6a 086; English 30C/107). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc

from spirit.game.session.effects import is_pokemon_tool


async def _strip_tools_then_hit(ctx):
    target = ctx.opponent_active()
    if target is not None and not ctx.effects_blocked(target):
        tools = [c for c in target.children if is_pokemon_tool(c)]
        if tools:
            await ctx.discard_cards(tools)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="fe5f88e5-94b7-50dc-bac1-b1e7720ed913",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zamazenta.Name",
    display_name="Zamazenta",
    searchable_by=["Zamazenta", "Basic"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=889,
    abilities=[
        Attack(
            title="Fend Off",
            game_text="Before doing damage, discard all Pokémon Tools from your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=_strip_tools_then_hit,
        ),
        Attack(
            title="Shield Press",
            game_text="During your opponent's next turn, this Pokémon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=pc.protect_next_turn(reduce=50),
        ),
    ],
)
