"""Drayton (SV085 172 -- JP SV7a 060; English PRE/172, SSP/174, SSP/232, SSP/244). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.session.effects import is_pokemon_card, is_trainer_card


async def drayton(ctx):
    top = list(ctx.deck_top(7))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    took = []
    mons = [c for c in top if is_pokemon_card(c)]
    if mons:
        took += await ctx.choose_cards(mons, 1, minimum=0, prompt="You may choose a Pokémon")
    trainers = [c for c in top if is_trainer_card(c)]
    if trainers:
        took += await ctx.choose_cards(trainers, 1, minimum=0, prompt="You may choose a Trainer card")
    if took:
        await ctx.put_in_hand(took)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="694034f7-cc6e-5f64-9319-460d95576020",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Drayton.Name",
    display_name="Drayton",
    searchable_by=["Drayton", "Supporter"],
    subtypes=["Supporter"],
    collector_number=172,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    effect=drayton,
)
