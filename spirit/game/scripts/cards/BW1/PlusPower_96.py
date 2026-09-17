"""PlusPower (BW - Black & White 96/114 -- JP BW1 051/053, the art here).

Item.

  "During this turn, your Pokemon's attacks do 10 more damage to the
   Active Pokemon (before applying Weakness and Resistance)."

Electropower without the type filter and at 10: one TurnDamageModifier
for every attacker of the player, opposing-Active only, this turn. Items
stack, so two PlusPowers are +20.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.passives import TurnDamageModifier


async def pluspower(ctx):
    """+10 to the opponent's Active from any of your attackers this turn."""
    ctx.add_turn_damage_modifier(TurnDamageModifier(10, ctx.player_id))
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.add_stat_visualization(
            pokemon, "Positive", "DamageDealtIncreased", card_text="+10 damage")


card = ItemCardDef(
    guid="fb6da855-6c8b-59ed-aed9-81ad28365cc0",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Item", "Plus Power"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=pluspower,
)
