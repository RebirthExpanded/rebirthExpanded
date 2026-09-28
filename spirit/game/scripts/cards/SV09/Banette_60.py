from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def cursed_words(ctx):
    """Your opponent chooses 3 cards from their hand and shuffles those cards
    into their deck."""
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    count = min(3, len(hand))
    picks = await ctx.choose_cards(
        hand, count, prompt="Choose 3 cards from your hand to shuffle into your deck.",
        player_id=ctx.opponent_id)
    if len(picks) < count:
        picks = list(picks) + [c for c in hand if c not in picks][:count - len(picks)]
    await ctx.shuffle_into_deck(picks, ctx.opponent_id)

card = PokemonCardDef(
    guid="c32df391-7fba-5e67-bf6c-4f3f72d2a21d",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Banette"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Attack(
            title="Cursed Words",
            game_text="Your opponent chooses 3 cards from their hand and shuffles those cards into their deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=0,
            effect=cursed_words,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
