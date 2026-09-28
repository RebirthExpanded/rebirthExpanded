from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def dig_it_up(ctx):
    """Look at the top card of your deck. You may discard that card."""
    top = ctx.deck_top(1)
    if not top:
        return
    idx = await ctx.present_card_choice(top[0], "Discard this card?", ["Discard", "Keep on top"])
    if idx == 0:
        await ctx.discard_cards([top[0]])

card = PokemonCardDef(
    guid="9697902b-96ac-576d-9612-11a07130994d",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    display_name="Rockruff",
    searchable_by=["Rockruff", "Basic", "Rockruff"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=744,
    abilities=[
        Attack(
            title="Dig It Up",
            game_text="Look at the top card of your deck. You may discard that card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=dig_it_up,
        ),
        Attack(
            title="Stampede",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
