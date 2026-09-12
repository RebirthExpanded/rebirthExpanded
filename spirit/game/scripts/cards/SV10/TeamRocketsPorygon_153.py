"""Team Rocket's Porygon (SV - Destined Rivals 153/182 -- JP SV10 081/099, the art here).

Basic Colorless Pokemon. HP 60, weakness Fighting x2, no resistance,
retreat 1.

  Hacking [C]  Discard a card from your hand. If you do, your opponent
               discards a card from their hand.

Both discards are the discarder's own choice.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef


async def hacking(ctx):
    mine = await ctx.discard_from_hand(1, minimum=1, prompt="Discard a card from your hand")
    if not mine:
        return
    if not ctx.hand(ctx.opponent_id):
        return
    await ctx.discard_from_hand(1, minimum=1, player_id=ctx.opponent_id,
                                prompt="Discard a card from your hand")


card = PokemonCardDef(
    guid="58f46e44-4b77-5075-a502-6a178dea6334",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygon.Name",
    display_name="Team Rocket's Porygon",
    searchable_by=["Team Rocket's Porygon", "Basic", "TeamRocketsPorygon"],
    subtypes=["Basic"],
    collector_number=153,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=137,
    abilities=[
        Attack(title="Hacking",
               game_text="Discard a card from your hand. If you do, your opponent discards a card from their hand.",
               cost={PokemonTypes.COLORLESS: 1}, effect=hacking),
    ],
)
