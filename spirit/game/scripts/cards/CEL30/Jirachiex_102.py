from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def wish_granter(ctx):
    """Draw cards until you have 7 cards in your hand."""
    await ctx.draw_until(7)


async def swift(ctx):
    """150, not affected by Weakness, Resistance or effects on the Active."""
    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True, ignore_target_effects=True)

card = PokemonCardDef(
    guid="433f423e-6197-5891-a18f-c11717bfaa8e",
    key="CEL30",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachiex.Name",
    display_name="Jirachi ex",
    searchable_by=["Jirachi ex", "Basic", "ex", "Jirachiex"],
    subtypes=["Basic", "ex"],
    collector_number=102,
    set_code="CEL30",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=385,
    abilities=[
        Attack(
            title="Wish Granter",
            game_text="Draw cards until you have 7 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=wish_granter,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=swift,
        ),
    ],
)
