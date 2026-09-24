from spirit.game.data_utils import SupporterCardDef
from spirit.game.card_effects.support_common import evolves_from, pokemon_can_still_evolve
from spirit.game.attributes import AttrID, Rarities


def _breeders_nurturing_condition(board, player_id):
    turn_state = getattr(board, "turn_state", None)
    if turn_state is None or turn_state.turn_number <= 2:
        return False
    # A target it could evolve: in play since an earlier turn, with an
    # evolution that can still come out of the deck (not every copy of it
    # in the discard pile).
    return any(
        turn_state.entered_play_turn.get(p.entity_id) != turn_state.turn_number
        and pokemon_can_still_evolve(board, player_id, p)
        for p in board.pokemon_in_play(player_id))


async def pokemon_breeders_nurturing(ctx):
    """Choose up to 2 of your Pokemon in play (not put into play this turn);
    for each, search the deck for a card that evolves from it and evolve it."""
    turn_state = ctx.session.turn_state
    candidates = [
        p for p in ctx.my_pokemon_in_play()
        if turn_state.entered_play_turn.get(p.entity_id) != turn_state.turn_number
    ]
    if not candidates:
        return
    targets = await ctx.choose_cards(
        candidates, 2, minimum=0,
        prompt="Choose up to 2 of your Pokémon in play to evolve.",
    )
    if not targets:
        return
    for target in targets:
        logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        if not logic_name:
            continue
        picks = await ctx.search_deck(
            lambda c, name=logic_name: evolves_from(c, name),
            count=1, minimum=0,
            prompt="Choose a card that evolves from that Pokémon.",
        )
        if picks:
            await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="133e9406-bed0-526d-9353-6742c96f626d",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonBreedersNurturing.Name",
    display_name="Pokémon Breeder's Nurturing",
    searchable_by=["Pokémon Breeder's Nurturing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=188,
    set_code="SWSH3",
    rarity=Rarities.RareUltra,
    effect=pokemon_breeders_nurturing,
    condition=_breeders_nurturing_condition
)
