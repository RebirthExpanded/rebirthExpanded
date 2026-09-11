"""Misty & Lorelei (SM - Cosmic Eclipse 199/236 -- JP SM12a 147/173).

TAG TEAM Supporter.

  "Search your deck for up to 3 [W] Energy cards, reveal them, and put them
   into your hand. Then, shuffle your deck.
   When you play this card, you may discard 5 other cards from your hand.
   If you do, during this turn, your [W] Pokemon can use their GX attacks
   even if you have used your GX attack this game."

The 5 cards are paid up front ("when you play this card"), before the
search. The allowance is a this-turn entry in TurnState.gx_reuse keyed on
the attacker's LIVE types, so a Stage 1 made Water by Vaporeon's Aqua
Effect gets its GX attack back too. The attack still counts as the
player's GX attack for the game.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_water_energy_card
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import is_pokemon_of_type


def _is_water_pokemon(pokemon) -> bool:
    return is_pokemon_of_type(pokemon, PokemonTypes.WATER)


async def misty_and_lorelei(ctx):
    if len(ctx.hand()) >= 5 and await ctx.ask_yes_no(
            "Discard 5 other cards from your hand so your [W] Pokémon can use "
            "their GX attacks this turn?"):
        paid = await ctx.discard_from_hand(5, prompt="Discard 5 cards for Misty & Lorelei")
        if len(paid) == 5:
            ctx.session.turn_state.allow_gx_reuse(ctx.player_id, _is_water_pokemon)
    picks = await ctx.search_deck(
        is_water_energy_card, count=3, minimum=0,
        prompt="Choose up to 3 [W] Energy cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="8b674dd7-d23b-5a15-a1d8-8d262ff1c002",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistyLorelei.Name",
    display_name="Misty & Lorelei",
    searchable_by=["Misty & Lorelei", "Supporter", "TAG TEAM", "MistyLorelei"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=199,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=misty_and_lorelei,
)
