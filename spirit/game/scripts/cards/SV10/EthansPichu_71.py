from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def zapping_draw(ctx):
    """30. Draw a card."""
    await ctx.deal_damage()
    await ctx.draw_cards(1)

card = PokemonCardDef(
    guid="658baa1e-1efc-592e-9065-538feea8f79b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansPichu.Name",
    display_name="Ethan's Pichu",
    searchable_by=["Ethan's Pichu", "Basic", "EthansPichu"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Zapping Draw",
            game_text="Draw a card.",
            cost={},
            damage=30,
            effect=zapping_draw,
        ),
    ],
)
