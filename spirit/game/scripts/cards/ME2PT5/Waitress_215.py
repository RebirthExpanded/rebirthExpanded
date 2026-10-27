"""Waitress (ME2PT5 215 -- JP MC 700; English ASC/215). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects.trainers import is_basic_energy_card


async def waitress(ctx):
    top = ctx.deck_top(6)
    if not top:
        return
    pool = [c for c in top if is_basic_energy_card(c)]
    picks = await ctx.choose_cards(pool, 1, minimum=0, display_cards=top,
                                   prompt="Choose a Basic Energy card to attach to 1 of your Pokémon.")
    if picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="71559417-dd5b-5d54-bc2c-c1f99c45fc18",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Waitress.Name",
    display_name="Waitress",
    searchable_by=["Waitress", "Supporter"],
    subtypes=["Supporter"],
    collector_number=215,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    effect=waitress,
)
