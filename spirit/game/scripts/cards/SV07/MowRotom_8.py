"""Mow Rotom (SV07 8 -- JP SV7 006; English SCR/8). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_pokemon_tool, is_special_energy


async def reaping_dash(ctx):
    target = ctx.opponent_active()
    if target is not None and not ctx.effects_blocked(target):
        junk = [c for c in target.children if is_pokemon_tool(c) or is_special_energy(c)]
        if junk:
            await ctx.discard_cards(junk)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="d74b20fa-05ce-59f4-8878-862402e493d3",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MowRotom.Name",
    display_name="Mow Rotom",
    searchable_by=["Mow Rotom", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=479,
    abilities=[
        Attack(
            title="Reaping Dash",
            game_text="Before doing damage, discard all Pokémon Tools and Special Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=reaping_dash,
        ),
    ],
)
