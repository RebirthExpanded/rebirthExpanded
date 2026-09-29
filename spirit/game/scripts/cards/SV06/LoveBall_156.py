"""Love Ball (SV - Twilight Masquerade 156/167 -- JP SV5a).

Item.

  "Search your deck for a Pokemon with the same name as 1 of your
   opponent's Pokemon in play, reveal it, and put it into your hand. Then,
   shuffle your deck."

Only a Pokemon card, and only the exact name: Pikachu ex on their side
doesn't find Pikachu, and a Snorlax Doll in play doesn't let it take the
Item Snorlax Doll. Mewtwo V-UNION in play finds any one of the four Mewtwo
V-UNION cards, which all carry that name.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_pokemon_card



def _deck_not_empty(board, player_id, card=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


def _name(card) -> str:
    return getattr(getattr(card, "card_obj", None), "display_name", None) or ""


async def love_ball(ctx):
    names = {_name(p) for p in ctx.opponent_pokemon_in_play() if is_pokemon_card(p)}
    names.discard("")
    picks = await ctx.search_deck(
        lambda c: is_pokemon_card(c) and _name(c) in names, count=1, minimum=0,
        prompt="Choose a Pokémon with the same name as 1 of your opponent's Pokémon.")
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="58faa7f8-24c5-5d70-bc55-178e77081733",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LoveBall.Name",
    display_name="Love Ball",
    searchable_by=['Love Ball', 'Item', 'LoveBall'],
    subtypes=['Item'],
    collector_number=156,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=_deck_not_empty,
    effect=love_ball,
)
