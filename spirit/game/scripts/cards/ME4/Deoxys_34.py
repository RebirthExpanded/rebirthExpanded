from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def psyspeed(ctx):
    """30. You may draw cards until you have 5 cards in your hand."""
    await ctx.deal_damage()
    if ctx.hand_size() < 5 and ctx.deck() and await ctx.ask_yes_no(
            "Draw cards until you have 5 cards in your hand?"):
        await ctx.draw_until(5)

card = PokemonCardDef(
    guid="81968ebd-6f15-5a1f-a270-aad7f027ccc1",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=386,
    abilities=[
        Attack(
            title="Psyspeed",
            game_text="You may draw cards until you have 5 cards in your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=psyspeed,
        ),
    ],
)
