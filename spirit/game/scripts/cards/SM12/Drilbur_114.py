from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _rototiller(ctx, count):
    """Shuffle `count` cards from your discard pile into your deck."""
    pool = list(ctx.recoverable_discard())
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(count, len(pool)),
                                   prompt=f"Choose {count} card(s) to shuffle into your deck")
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.shuffle_into_deck(picks, ctx.player_id)


async def rototiller(ctx):
    await _rototiller(ctx, 1)

card = PokemonCardDef(
    guid="158e0416-3068-5aab-9975-c8b74d8942ef",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    display_name="Drilbur",
    searchable_by=["Drilbur", "Basic", "Drilbur"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=529,
    abilities=[
        Attack(
            title="Rototiller",
            game_text="Shuffle a card from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=rototiller,
        ),
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
