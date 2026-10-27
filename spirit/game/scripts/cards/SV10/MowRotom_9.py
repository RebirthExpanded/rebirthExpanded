"""Mow Rotom (SV10 9 -- JP SV10 004; English DRI/9). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import full_stack, is_pokemon_tool


async def gadget_show(ctx):
    """30 for each Pokemon Tool attached to all of your Pokemon."""
    tools = sum(1 for p in ctx.my_pokemon_in_play()
                for c in full_stack(p) if c is not p and is_pokemon_tool(c))
    if tools:
        await ctx.deal_damage(30 * tools)


async def trimming_mower(ctx):
    await ctx.deal_damage()
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="dd89608a-fe1b-5e1f-85e9-f20a2d45433d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MowRotom.Name",
    display_name="Mow Rotom",
    searchable_by=["Mow Rotom", "Basic"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=479,
    abilities=[
        Attack(
            title="Trimming Mower",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=trimming_mower,
        ),
        Attack(
            title="Gadget Show",
            game_text="This attack does 30 damage for each Pokémon Tool attached to all of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=gadget_show,
        ),
    ],
)
