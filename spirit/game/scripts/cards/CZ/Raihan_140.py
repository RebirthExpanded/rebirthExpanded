from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _raihan_search(ctx, picks):
    found = await ctx.search_deck(
        count=1, minimum=0,
        prompt="Search your deck for a card and put it into your hand.",
    )
    await ctx.put_in_hand(found, reveal=False)
    await ctx.shuffle_deck()


def _raihan_condition(board, player_id):
    """A Pokemon of mine was Knocked Out during the opponent's last turn,
    and there is a basic Energy card in my discard pile to attach."""
    if not board.turn_state.pokemon_lost_last_turn(player_id):
        return False
    discard = board.find_player_area(player_id, "discard")
    return any(is_basic_energy_card(c) for c in (discard.children if discard else []))


card = SupporterCardDef(
    guid="cc0d13f8-938c-5a84-96d8-e9cc96b22bb1",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Raihan.Name",
    display_name="Raihan",
    searchable_by=["Raihan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=140,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    condition=_raihan_condition,
    effect=attach_from_discard(
        predicate=is_basic_energy_card, count=1, target="choice",
        prompt="Attach a basic Energy card from your discard pile to 1 of your Pokémon.",
        then=_raihan_search,
    ),
)
