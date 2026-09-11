"""Mallow & Lana (SM - Cosmic Eclipse 198/236 -- JP SM12 095/098).

Supporter (TAG TEAM).

  "Switch your Active Pokemon with 1 of your Benched Pokemon.
   When you play this card, you may discard 2 other cards from your hand.
   If you do, heal 120 damage from the Pokemon you moved to your Bench."

The switch is the card; the heal is bought with 2 other cards, asked
before anything moves ("when you play this card") and paid then, with the
heal landing on the Pokemon that just left the Active spot.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import player_has_bench
from spirit.game.data_utils import SupporterCardDef


async def mallow_and_lana(ctx):
    paid = False
    if len(ctx.hand()) >= 2 and await ctx.ask_yes_no(
            "Discard 2 other cards from your hand to heal 120 damage from "
            "the Pokémon you move to your Bench?"):
        paid = len(await ctx.discard_from_hand(
            2, prompt="Discard 2 cards for Mallow & Lana")) == 2
    old_active = ctx.my_active()
    target = await ctx.choose_pokemon(ctx.my_bench(), "Choose your new Active Pokémon")
    if target is None:
        return
    if not await ctx.switch_active(ctx.player_id, target):
        return
    if paid and old_active is not None:
        await ctx.heal(120, old_active)


card = SupporterCardDef(
    guid="da37abc0-cbb7-52a0-a35e-ffc34e8d2cec",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MallowLana.Name",
    display_name="Mallow & Lana",
    searchable_by=["Mallow & Lana", "Supporter", "TAG TEAM", "MallowLana"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=198,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=mallow_and_lana,
    condition=player_has_bench,
)
