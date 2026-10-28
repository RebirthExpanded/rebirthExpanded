"""Miriam (SV1 179 -- JP SV1V 077; English SVI/179, SVI/238, SVI/251). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.session.effects import is_pokemon_card


def _mons_in_discard(board, player_id, card=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_pokemon_card(c) for c in discard.children)


async def miriam(ctx):
    pool = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(5, len(pool)), minimum=0, prompt="Shuffle up to 5 Pokémon into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)
        await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="c106d1c8-7bae-540d-b3fc-058fc98f5b6e",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Miriam.Name",
    display_name="Miriam",
    searchable_by=["Miriam", "Supporter"],
    subtypes=["Supporter"],
    collector_number=179,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_mons_in_discard,
    effect=miriam,
)
