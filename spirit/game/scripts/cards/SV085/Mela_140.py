"""Mela (SV085 140 -- JP SV4K 066; English PAR/167, PAR/236, PAR/254, PRE/140). Japanese art.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)



def _lost_last_turn(board, player_id, card=None) -> bool:
    ts = getattr(board, "turn_state", None)
    return ts is not None and bool(ts.kos_suffered_last_turn.get(player_id))


async def mela(ctx):
    pool = [c for c in ctx.discard_pile() if _basic_fire(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Fire Energy card to attach")
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon") if picks else None
    if target is not None and await ctx.attach_energy(picks[0], target):
        await ctx.draw_until(6)


card = SupporterCardDef(
    guid="b4ec6812-fd9d-52d2-b39a-957b4300315e",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mela.Name",
    display_name="Mela",
    searchable_by=["Mela", "Supporter"],
    subtypes=["Supporter"],
    collector_number=140,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareUltra,
    condition=_lost_last_turn,
    effect=mela,
)
