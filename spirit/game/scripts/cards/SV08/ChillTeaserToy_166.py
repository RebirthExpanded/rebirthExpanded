"""Chill Teaser Toy (SV08 166 -- JP SV8 096; English SSP/166). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.card_effects.trainers import second_players_first_turn


async def chill_teaser_toy(ctx):
    pool = [e for p in ctx.opponent_pokemon_in_play() for e in ctx.attached_energies(p)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to put into your opponent's hand")
        if picks:
            await ctx.put_in_hand(picks)


card = ItemCardDef(
    guid="91fcdbee-af2c-5325-8554-28c72c2cefd8",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChillTeaserToy.Name",
    display_name="Chill Teaser Toy",
    searchable_by=["Chill Teaser Toy", "Item"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=second_players_first_turn,
    effect=chill_teaser_toy,
)
