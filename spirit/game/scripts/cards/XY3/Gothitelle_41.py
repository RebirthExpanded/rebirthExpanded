from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_stadium_card


def _stadium_in_play(board, player_id, pokemon=None) -> bool:
    area = board.find_global_area("activeStadium")
    return bool(area and area.children)


def _name(card) -> str:
    return getattr(getattr(card, "card_obj", None), "display_name", "") or ""


async def teleport_room(ctx):
    """Discard the Stadium in play, then put a Stadium with a different name
    from your discard pile into play -- Neutralization Zone included: it
    can't go to the hand or deck from there, but into play it may."""
    stadium = ctx.stadium_in_play()
    if stadium is None:
        return
    gone = _name(stadium)
    if await ctx.discard_stadium() is None:
        return
    pool = [c for c in ctx.discard_pile() if is_stadium_card(c) and _name(c) != gone]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1,
                                   prompt="Choose a Stadium card to put into play.")
    if picks:
        await ctx.put_stadium_into_play(picks[0])


async def psy_report(ctx):
    """60. Your opponent reveals their hand."""
    await ctx.deal_damage()
    await ctx.reveal_hand(ctx.opponent_id)

card = PokemonCardDef(
    guid="b5fc09bf-d939-5b9c-b0b4-b31b55938c40",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle", "Stage 2", "Gothitelle"],
    subtypes=["Stage 2"],
    collector_number=41,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    family_id=574,
    abilities=[
        Ability(
            title="Teleport Room",
            game_text="Once during your turn (before your attack), you may discard any Stadium card in play. If you do, put a Stadium card with a different name from your discard pile into play.",
            activation=Activations.ONCE_PER_TURN,
            condition=_stadium_in_play,
            effect=teleport_room,
        ),
        Attack(
            title="Psy Report",
            game_text="Your opponent reveals his or her hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=psy_report,
        ),
    ],
)
