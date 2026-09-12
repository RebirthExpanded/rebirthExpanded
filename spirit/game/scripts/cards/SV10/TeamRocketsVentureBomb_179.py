"""Team Rocket's Venture Bomb (SV - Destined Rivals 179/182 -- JP SV10 089/099, the art here).

Item.

  "Flip a coin. If heads, put 2 damage counters on 1 of your opponent's
   Pokemon. If tails, put 2 damage counters on your Active Pokemon."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef


async def venture_bomb(ctx):
    heads = await ctx.flip_coins(1, "Team Rocket's Venture Bomb")
    if heads and heads[0]:
        targets = ctx.opponent_pokemon_in_play()
        if not targets:
            return
        target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon")
        if target is None:
            return
    else:
        target = ctx.my_active()
        if target is None:
            return
    await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)


card = ItemCardDef(
    guid="4c8adf9e-b573-5608-9133-4fbf6318a2ac",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsVentureBomb.Name",
    display_name="Team Rocket's Venture Bomb",
    searchable_by=["Team Rocket's Venture Bomb", "Item", "TeamRocketsVentureBomb", "Team Rocket's"],
    subtypes=["Item"],
    collector_number=179,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=venture_bomb,
)
