"""Mesagoza (SV1 178 -- JP SV1V 078; English SVI/178). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import StadiumCardDef

from spirit.game.data_utils import Ability, Activations
from spirit.game.session.effects import is_pokemon_card


def _mesagoza_condition(board, player_id, card=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def mesagoza(ctx):
    results = await ctx.flip_coins(1, "Mesagoza")
    if results and results[0]:
        picks = await ctx.search_deck(is_pokemon_card, count=1, minimum=0, prompt="Choose a Pokémon to put into your hand.")
        if picks:
            await ctx.put_in_hand(picks)
        await ctx.shuffle_deck()


card = StadiumCardDef(
    guid="56e7d0a8-7dcc-5926-8c20-0978a89c9244",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mesagoza.Name",
    display_name="Mesagoza",
    searchable_by=["Mesagoza", "Stadium"],
    subtypes=["Stadium"],
    collector_number=178,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Mesagoza",
        game_text="Once during each player's turn, that player may flip a coin. If heads, that player searches their deck for a Pokémon, reveals it, and puts it into their hand. Then, that player shuffles their deck.",
        activation=Activations.ONCE_PER_TURN,
        effect=mesagoza,
        condition=_mesagoza_condition,
    ),
)
