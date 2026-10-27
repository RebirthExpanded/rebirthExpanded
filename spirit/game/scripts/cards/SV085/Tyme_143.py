"""Tyme (SV085 143 -- JP SV8a 193; English PRE/143, SSP/190). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.effects import is_pokemon_card


def _has_hand_mon(board, player_id, card=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_pokemon_card(c) for c in hand.children)


async def tyme(ctx):
    pool = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Pokémon in your hand")
    if not picks:
        return
    mon = picks[0]
    hundreds = await ctx.choose("Guess the Pokémon's HP (hundreds)", ["0", "100", "200", "300"], player_id=ctx.opponent_id)
    tens = await ctx.choose("Guess the Pokémon's HP (tens)", [str(10 * i) for i in range(10)], player_id=ctx.opponent_id)
    guess = 100 * (hundreds if isinstance(hundreds, int) else 0) + 10 * (tens if isinstance(tens, int) else 0)
    await ctx.reveal_cards([mon])
    if guess == (mon.get_attribute(AttrID.HP, 0) or 0):
        await ctx.draw_cards(4, player_id=ctx.opponent_id)
    else:
        await ctx.draw_cards(4)


card = SupporterCardDef(
    guid="d2c3351b-4862-5ef7-bc69-653e39d9f82d",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tyme.Name",
    display_name="Tyme",
    searchable_by=["Tyme", "Supporter"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareUltra,
    condition=_has_hand_mon,
    effect=tyme,
)
