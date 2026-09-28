from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack, is_pokemon_tool


async def manual_wash(ctx):
    """20. Heal 10 damage from each of your Pokemon."""
    await ctx.deal_damage()
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.heal(10, pokemon)


async def gadget_show(ctx):
    """30 for each Pokemon Tool attached to all of your Pokemon."""
    tools = sum(1 for p in ctx.my_pokemon_in_play()
                for c in full_stack(p) if c is not p and is_pokemon_tool(c))
    if tools:
        await ctx.deal_damage(30 * tools)

card = PokemonCardDef(
    guid="5cd6a046-c061-5ff5-beb8-7453e4f5fdae",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WashRotom.Name",
    display_name="Wash Rotom",
    searchable_by=["Wash Rotom", "Basic", "WashRotom"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=479,
    abilities=[
        Attack(
            title="Manual Wash",
            game_text="Heal 10 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=manual_wash,
        ),
        Attack(
            title="Gadget Show",
            game_text="This attack does 30 damage for each Pok\u00e9mon Tool attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=gadget_show,
        ),
    ],
)
