"""Melmetal (SV07 104 -- JP SV7 071; English SCR/104). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_pokemon_tool


async def reforged_axe(ctx):
    tools = [c for c in ctx.attacker.children if is_pokemon_tool(c)]
    if not tools:
        return
    await ctx.discard_cards(tools)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="dd738dd4-4768-54cf-9b43-856f18ed30f7",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetal.Name",
    display_name="Melmetal",
    searchable_by=["Melmetal", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Attack(
            title="Wrack Down",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Reforged Axe",
            game_text="Before doing damage, discard all Pokémon Tools from this Pokémon. If you can't discard any, this attack does nothing.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=250,
            effect=reforged_axe,
        ),
    ],
)
