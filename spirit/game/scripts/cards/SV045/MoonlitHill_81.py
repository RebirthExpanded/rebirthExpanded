"""Moonlit Hill (SV045 81 -- JP SV8a 183; English PAF/81). Japanese art.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import StadiumCardDef

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_psychic(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.PSYCHIC)

from spirit.game.data_utils import Ability, Activations


def _moonlit_condition(board, player_id, card=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_basic_psychic(c) for c in hand.children)


async def moonlit_hill(ctx):
    paid = await ctx.discard_from_hand(1, minimum=1, predicate=_basic_psychic, prompt="Discard a Basic Psychic Energy card")
    if paid:
        for p in ctx.my_pokemon_in_play():
            await ctx.heal(30, p)


card = StadiumCardDef(
    guid="fc348ef9-1223-54b1-a826-cdde1c24e8a5",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MoonlitHill.Name",
    display_name="Moonlit Hill",
    searchable_by=["Moonlit Hill", "Stadium"],
    subtypes=["Stadium"],
    collector_number=81,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Moonlit Hill",
        game_text="Once during each player's turn, that player may discard a Basic Psychic Energy card from their hand in order to heal 30 damage from each of their Pokémon.",
        activation=Activations.ONCE_PER_TURN,
        effect=moonlit_hill,
        condition=_moonlit_condition,
    ),
)
