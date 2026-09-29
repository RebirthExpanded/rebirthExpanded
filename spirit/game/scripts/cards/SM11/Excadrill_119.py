from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _rototiller(ctx, count):
    """Shuffle `count` cards from your discard pile into your deck."""
    pool = list(ctx.discard_pile())
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(count, len(pool)),
                                   prompt=f"Choose {count} card(s) to shuffle into your deck")
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.shuffle_into_deck(picks, ctx.player_id)


async def rototiller(ctx):
    await _rototiller(ctx, 4)

card = PokemonCardDef(
    guid="a22fec38-79f3-5b02-9f34-691d3da0f65c",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name",
    display_name="Excadrill",
    searchable_by=["Excadrill", "Stage 1", "Excadrill"],
    subtypes=["Stage 1"],
    collector_number=119,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    family_id=529,
    abilities=[
        Attack(
            title="Rototiller",
            game_text="Shuffle 4 cards from your discard pile into your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=0,
            effect=rototiller,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
