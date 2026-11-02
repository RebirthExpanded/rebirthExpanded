"""Player's Ceremony (SPJ 127 -- JP SP 127; English Japan only). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef

from spirit.game.data_utils import Ability, Activations


def _ceremony_condition(board, player_id, stadium=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def players_ceremony(ctx):
    """Draw 2 cards. If you do, your turn ends."""
    drawn = await ctx.draw_cards(2)
    if drawn:
        ctx.ends_turn = True


PLAYERS_CEREMONY_ABILITY = Ability(
    title="Player's Ceremony",
    game_text="Once during each player's turn, that player may draw 2 cards. If they do, their turn ends.",
    activation=Activations.ONCE_PER_TURN,
    condition=_ceremony_condition,
    effect=players_ceremony,
)


card = StadiumCardDef(
    guid="59257ef9-e866-586d-961c-77331b25b95e",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlayersCeremony.Name",
    display_name="Player's Ceremony",
    searchable_by=["Player's Ceremony", "Stadium"],
    subtypes=["Stadium"],
    collector_number=127,
    set_code="SPJ",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    ability=PLAYERS_CEREMONY_ABILITY,
)
