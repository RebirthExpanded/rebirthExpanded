"""Energy Coin (SV - Black Bolt 81/86 -- JP SV11B 079/086).

Item.

  "Flip 2 coins. If both of them are heads, search your deck for a Basic
   Energy card and attach it to 1 of your Pokemon. Then, shuffle your
   deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_basic_energy


async def energy_coin(ctx):
    results = await ctx.flip_coins(2, "Energy Coin")
    if not all(results):
        return
    picks = await ctx.search_deck(is_basic_energy, count=1, minimum=0,
                                  prompt="Choose a Basic Energy card to attach.")
    if picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(),
                                          "Choose a Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="6e4dfe69-2335-55c0-ad50-09af8f44f448",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyCoin.Name",
    display_name="Energy Coin",
    searchable_by=["Energy Coin", "Item", "EnergyCoin"],
    subtypes=["Item"],
    collector_number=81,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=energy_coin,
)
