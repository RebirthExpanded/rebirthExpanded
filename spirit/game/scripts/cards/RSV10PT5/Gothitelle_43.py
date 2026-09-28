from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.pokemon import in_active_spot


async def distorted_future(ctx):
    """The opponent shuffles their hand into their deck and draws 3 cards."""
    opp = ctx.opponent_id
    hand = list(ctx.hand(opp))
    if hand:
        await ctx.shuffle_into_deck(hand, opp)
    else:
        await ctx.shuffle_deck(opp)
    await ctx.draw_cards(3, opp)


def _same_hand_size(ctx) -> bool:
    return ctx.hand_size() == ctx.hand_size(ctx.opponent_id)

card = PokemonCardDef(
    guid="38a8678a-3e7e-5fcc-a619-81cfce0dbdfa",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle", "Stage 2", "Gothitelle"],
    subtypes=["Stage 2"],
    collector_number=43,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    family_id=574,
    abilities=[
        Ability(
            title="Distorted Future",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may have your opponent shuffle their hand into their deck and draw 3 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=distorted_future,
        ),
        Attack(
            title="Synchro Shot",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=bonus_if(_same_hand_size, 90),
        ),
    ],
)
